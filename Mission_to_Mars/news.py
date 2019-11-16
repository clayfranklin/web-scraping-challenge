import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup

url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

def news_scrape():

    response = requests.get(url)

    soup = BeautifulSoup(response.text,'html.parser')

    # results = soup.find_all(class_="content_title")
    results_1 = soup.find_all(class_="slide")
    results_1

    news_titles = []
    paragraphs = []
    for result in results_1:
        news_title = result.find(class_="content_title").text
        news_titles.append(news_title)
        news_p = result.find(class_="rollover_description_inner").text
        paragraphs.append(news_p)
    news_title=news_title.strip()
    news_p=news_p.strip()
    # news_article = print(f'{news_title}.  {news_p}')
    return news_title, news_p
    
