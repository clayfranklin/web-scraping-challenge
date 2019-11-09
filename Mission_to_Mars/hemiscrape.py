from splinter import Browser
from bs4 import BeautifulSoup


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': "C:/Users/clayf/Documents/web-scraping-challenge/Mission_to_Mars/chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    image=soup.find_all('img')[5]['src']
    img_img = ("https://astrogeology.usgs.gov"+image)   

    image_urls = [
    # # {"title": "Valles Marineris Hemisphere", "img_url": tiff_path},
    {"title": "Cerberus Hemisphere", "img_url": img_img}
    # # {"title": "Schiaparelli Hemisphere", "img_url": img_pathway},
    # # {"title": "Syrtis Major Hemisphere", "img_url": image_path},
    ]

    browser.quit()

    return image_urls