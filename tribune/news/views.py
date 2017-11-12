from django.http import HttpResponse
from django.shortcuts import render
import datetime as dt

# Create your views here.
def welcome(request):
    '''
    View function for the root page
    '''
    return HttpResponse('Welcome to Moringa Tribune')

def news_of_day(request):
    '''
    View function for the news of the current day
    '''
    date = dt.date.today()

    # Convert date object to find exact day
    day = convert_dates(date)

    html = f'''
        <html>
            <body>
                <h1> News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

def convert_dates(dates):
    '''
    Function that takes a date object and returns the day of the week

    Args:
        date : date object

    Returns:
        day : day of the week
    '''
    # Get week day number from the date
    day_number = dt.date.weekday(dates)

    # List of days of the week
    days = ['Monday', 'Tuesday', 'Wednewday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    # Actual day of the week to be returned
    day = days[day_number]

    return day


