from splinter import Browser
from bs4 import BeautifulSoup


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': "web-scraping-challenge/Mission_to_Mars/chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


def Hemisphere():
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    Browser.visit(url)
    Browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')

    html = Browser.html
    soup = BeautifulSoup(html, 'html.parser')

    Browser.visit(url)
    Browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
    html = Browser.html
    soup = BeautifulSoup(html, 'html.parser')
    image=soup.find_all('img')[5]['src']
    img_img = ("https://astrogeology.usgs.gov"+image)   

    hemisphere_image_urls = [
    # {"title": "Valles Marineris Hemisphere", "img_url": tiff_path},
    {"title": "Cerberus Hemisphere", "img_url": img_img}
    # {"title": "Schiaparelli Hemisphere", "img_url": img_pathway},
    # {"title": "Syrtis Major Hemisphere", "img_url": image_path},
    ]
    return hemisphere_image_urls


    # url = "https://nashville.craigslist.org/search/hhh?max_price=20000&availabilityMode=0"
    # browser.visit(url)

    # html = browser.html
    # soup = BeautifulSoup(html, "html.parser")

    # listings["headline"] = soup.find("a", class_="result-title").get_text()
    # listings["price"] = soup.find("span", class_="result-price").get_text()
    # listings["hood"] = soup.find("span", class_="result-hood").get_text()

    # return listings
