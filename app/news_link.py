import requests
import json
import os
from dotenv import load_dotenv
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key=os.getenv("NEWS_API_KEY"))

print('Please enter three keywords or topics you are interested in.')
print('Please note that no keyword can be over 13 characters long')


keyword_1 = input("First Keyword: ")
if len(keyword_1) > 13:
    print("Sorry, your keyword was too long. Please run the search again.")
    quit()
keyword_2 = input("Second Keyword: ")
if len(keyword_2) > 13:
    print("Sorry, your keyword was too long. Please run the search again.")
    quit()
keyword_3 = input("Third Keyword: ")
if len(keyword_3) > 13:
    print("Sorry, your keyword was too long. Please run the search again.")
    quit()
print('Your keywords are:', keyword_1, keyword_2, keyword_3)

print('If you dont want articles from too long ago, please enter a starting year. Otherwise you can enter N/A.')

start_year = input('Year: ')
if str("N/A") in start_year:
    print('You do not want a year parameter.')
elif len(start_year) == 4 and start_year.isdigit() and int(start_year) < 2022:
    print('Your starting year is: ', start_year)
else:
    print("There was an issue with your date. Please try the search again.")
    quit()
