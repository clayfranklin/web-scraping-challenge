import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

def weather_scraper():
    url = "https://twitter.com/marswxreport?lang=en"

    response = requests.get(url)

    soup = BeautifulSoup(response.text,'html.parser')

    results_1 = soup.find(class_="content")
    results_2 = results_1.find(class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    weather = results_2.strip('()\n')
    weather = weather.strip('InSight')
    weather = weather.strip('')
    mars_twitter = weather.strip('\n')
    mars_twitter = mars_twitter.strip('hPapic.twitter.com/VxWNunPM5q')

    return mars_twitter
