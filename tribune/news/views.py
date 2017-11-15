from django.http import HttpResponse, Http404
from django.shortcuts import render,redirect
import datetime as dt
from .models import Article, tags

# Create view functions here
def news_today(request):
    '''
    View function for the news of the current day
    '''
    date = dt.date.today()
    news = Article.todays_news()
    # news_tags = []
    # for single_news in news:
    #     news_tags = tags.filter(id=single_news.id).all()

    return render(request, 'all-news/today-news.html', {"date":date,"news":news})

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

def article(request,article_id):
    '''
    View function to display a single article
    '''
    try:
        article = Article.objects.get(id=article_id)
        tags = article.tags.all()
    except DoesNotExist:
        raise Http404()

    return render(request, 'all-news/article.html', {"article":article, "tags":tags})





