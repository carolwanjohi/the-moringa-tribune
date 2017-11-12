from django.http import HttpResponse, Http404
from django.shortcuts import render,redirect
import datetime as dt

# Create functions here
# def convert_dates(dates):
#     '''
#     Function that takes a date object and returns the day of the week

#     Args:
#         date : date object

#     Returns:
#         day : day of the week
#     '''
#     # Get week day number from the date
#     day_number = dt.date.weekday(dates)

#     # List of days of the week
#     days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

#     # Actual day of the week to be returned
#     day = days[day_number]

#     return day

# Create your views here.
def welcome(request):
    '''
    View function for the root page
    '''
    return render(request, 'welcome.html')

def news_today(request):
    '''
    View function for the news of the current day
    '''
    date = dt.date.today()

    return render(request, 'all-news/today-news.html', {"date":date,})

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


    return render(request, 'all-news/past-news.html', {"date":date})




