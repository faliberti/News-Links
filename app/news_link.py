import requests
import json
import os
import datetime as dt
import pandas as pd
from dotenv import load_dotenv
from newsapi import NewsApiClient

load_dotenv()
newsapikey = os.getenv("NEWS_API_KEY")

def user_sorting():
    '''
    Obtains sorting method chosen by user (Relevancy, Popularity, or Newest).

    No parameters

    Returns the user sorting option.
    '''

    print('You can sort the search results by relevancy, popularity, or the newest published. Please choose one of relevancy, popularity, newest to sort your articles.')
    user_sort_choice = input('Enter your sorting choice: ')
    choice_options = ['relevancy', 'popularity', 'newest']
    if user_sort_choice.lower() in choice_options:
        print('You sorted by: ', user_sort_choice)
    else:
        print('You did not choose a correct sorting option.')
        quit()
    if user_sort_choice.lower() == str('newest'):
        user_sort_choice = str('publishedAt')
    return user_sort_choice

user_sorting_choice = user_sorting()

def get_user_dates():
    '''
    Obtains the correct start and end dates for the time period the user would like to search articles from.

    No parameters

    Returns Year, Month, and Day into the correct format of ISO 8601.
    '''

    user_year = input('Year: ')
    if str("N/A") in user_year:
        print('You do not want a date parameter.')
    elif len(user_year) == 4 and user_year.isdigit() and int(user_year) < 2022:
        try:
            user_month = input('Month: ')
            if len(user_month) < 3 and len(user_month) > 0 and user_month.isdigit() and int(user_month) < 13:
                user_day = input('Day: ')
                if len(user_day) <3 and len(user_day) > 0 and user_day.isdigit() and int(user_day) < 32:
                    user_date_1 = dt.date(int(user_year), int(user_month), int(user_day))
                    if user_date_1 > dt.date.today():
                        quit()
                    else:
                        user_date_1 = user_date_1.isoformat()
                else:
                    print("There was an issue with your day. Please try the search again.")
                    quit()
            else:
                print("There was an issue with your month. Please try the search again.")
                quit()
        except:
            print("There was an issue with your date. Please try the search again.")
            quit()
    else:
        print("There was an issue with your year. Please try the search again.")
        quit()
    return user_date_1

def get_article_links(keyword, user_start_date, user_end_date, sorting_choice):
    '''
    Fetches article links from the News API, for keywords and starting year.

    Params:
        keyword (str) the requested keyword(s), like "Tesla"
        user_start_date (date object) the requested starting search date, like "2021/05/04"
        user_end_date (date object) the requesting ending search date, like "2021/05/14"
        sorting_choice (str) the user choice for sorting, like "newest"

    Example:
        result = get_article_links(keyword='tesla', user_start_date=startdate, user_end_date=enddate, sorting_choice='newest')

    Prints my_news (list)
    Returns the dictionary news
    '''

    user_api=newsapikey
    api_url = f'https://newsapi.org/v2/everything?q={keyword}&from={user_start_date}&to={user_end_date}&sortBy={sorting_choice}&apiKey={user_api}'
    news = requests.get(api_url).json()
    
    articles = news["articles"]
    
    my_articles = []
    my_news = ""

    for article in articles:
        my_articles.append(article["url"])

    if len(my_articles) < 3:
        print("Sorry, couldn't find enough links for those criteria.")
        exit()

    for i in range(3):
        my_news = my_news + my_articles[i] + '\n'
    
    print(my_news)
    return news

if __name__ == "__main__":

    print('Please enter a keyword or phrase on a topic you are interested in. Example: iphone x review')
    print('Please note that no keyword or phrase can be over 100 characters long')

    keywords = input("Keyword or Phrase: ")
    if len(keywords) > 100:
        print("Sorry, your keyword was too long. Please run the search again.")
        quit()

    print('You can enter date parameters for the time period the article was written. First is your start date, and second is your end date. Please enter values in the form of YYYY, MM, DD. You can enter N/A if you dont want a start or end date. Important Note: if you have the free version of the API, you can only go back one month from today\'s date.')

    start_date = get_user_dates()
    end_date = get_user_dates()

    if start_date > end_date:
        print('Your end date is before your start date. Please try your search again.')
        quit()
    

    get_article_links(keyword=keywords, user_start_date=start_date, user_end_date=end_date, sorting_choice=user_sorting_choice)
