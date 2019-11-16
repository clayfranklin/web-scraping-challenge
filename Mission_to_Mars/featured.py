from splinter import Browser
from bs4 import BeautifulSoup

def img_finder():
    executable_path = {'executable_path': "C:/Users/clayf/Documents/web-scraping-challenge/Mission_to_Mars/chromedriver.exe"}
    browser = Browser('chrome', **executable_path, headless=False)

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    ftrd_img = soup.find(class_='slide')
    url = ftrd_img.find('a')['data-fancybox-href']
    featured_img_url = ("https://www.jpl.nasa.gov"+url)

    browser.quit()
     

    return featured_img_url