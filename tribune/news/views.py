from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect
import datetime as dt
from .models import Article, tags, NewsLetterRecipients, MoringaMerch
from .forms import NewsLetterForm, NewsArticleForm
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MerchSerializer

# Create view functions here
def news_today(request):
    '''
    View function for the news of the current day and form for subscribing to News Letters
    '''
    date = dt.date.today()
    news = Article.todays_news()
    news_tags = tags.get_tags()
    form = NewsLetterForm()

    # news_tags = []
    # for single_news in news:
    #     news_tags = tags.filter(id=single_news.id).all()

    # Old NewsLetterForm
    # if request.method == 'POST':

    #     form = NewsLetterForm(request.POST)

    #     if form.is_valid():
    #         name = form.cleaned_data['your_name']

    #         email = form.cleaned_data['email']

    #         recipient = NewsLetterRecipients(name=name, email=email)

    #         recipient.save()

    #         send_welcome_email(name,email)

    #         # return HttpResponseRedirect('news_today')
    #         return redirect(news_today)

    # else:

        # form = NewsLetterForm()

    return render(request, 'all-news/today-news.html', {"date":date,"news":news,"letterForm":form})


def past_days_news(request,past_date):
    '''
    View function to return news from past dates
    '''
    try:

        # Convert data from the string url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        # Redirect to news_today
        return redirect(news_today)

    news = Article.days_news(date)
    return render(request, 'all-news/past-news.html', {"date":date,"news":news})

def search_results(request):
    '''
    View function to display search results
    '''
    # Check if article query exists and if it has a value
    if 'article' in request.GET and request.GET['article']:
        search_term = request.GET.get('article')
        searched_articles = Article.search_by_title(search_term)
        message = f'{search_term}'
        return render(request, 'all-news/search.html', {"message":message,"articles":searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html', {"message":message})

# Restrict view to only authorised users
@login_required(login_url='/accounts/login')
def article(request,article_id):
    '''
    View function to display a single article to authenticated logged in users
    '''
    try:
        article = Article.objects.get(id=article_id)
        tags = article.tags.all()
    except DoesNotExist:
        raise Http404()

    return render(request, 'all-news/article.html', {"article":article, "tags":tags})

def tag(request,tag_id):
    '''
    View function to display a single tag and its articles
    '''
    try:
        tag = tags.objects.get(id=tag_id)
        articles = Article.objects.filter(tags=tag).all()
    except DoesNotExist:
        raise Http404()
    title = f'{tag}'
    return render(request, 'all-news/tag.html', {"tag":tag, "articles":articles, "title":title})

# Restrict view to only authorised users
@login_required(login_url='/accounts/login')
def new_article(request):
    '''
    View function to display a form for creating a new article to authenticated logged in users
    '''
    current_user = request.user
    if request.method == 'POST':
        # request.FILES cause an article has an image
        form = NewsArticleForm(request.POST, request.FILES)
        if form.is_valid:
            article = form.save(commit=False)
            article.editor = current_user
            article.save()
            # article.tags.save()
            return redirect(news_today)

    else:
        form = NewsArticleForm()
    return render(request, 'new_article.html', {"form":form})

def newsletter(request):
    '''
    Function that asynchronously saves the news letter recipient to the database and sends a welcome email
    '''
    name = request.POST.get('your_name')
    email = request.POST.get('email')

    recipient = NewsLetterRecipients(name=name, email=email)
    recipient.save()

    send_welcome_email(name,email)

    data = {'success':'You have been successfully added to the mailing list'}

    return JsonResponse(data)

class MerchList(APIView):
    '''
    API view to handle requests
    '''
    def get(self, request, format=None):
        '''
        Get method where we query the database to get all MoringaMerch objects, serialize the data and return the serialized data as the response
        '''
        all_merch = MoringaMerch.objects.all()
        serializers = MerchSerializer(all_merch, many=True)
        return Response(serializers.data)











