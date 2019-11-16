import pandas as pd

def fact_scrape():
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)

    df2=tables[1]
    df1 = df2.drop(columns=['Earth'])
    df3 = df1.rename(columns={"Mars - Earth Comparison":"Description"})
    
    df=tables[0]
    df.columns = ['Description', 'Mars']
  
    df_mars = pd.concat([df3, df])
    df_mars.reset_index([])
    mars_facts = df_mars.drop([df_mars.index[0], df_mars.index[1] , df_mars.index[2]])
    mars_facts = mars_facts.to_dict(orient = "records")
    return mars_facts



# def init_browser():
#     # @NOTE: Replace the path with your actual path to the chromedriver
#     executable_path = {'executable_path': "C:/Users/clayf/Documents/web-scraping-challenge/Mission_to_Mars/chromedriver.exe"}
#     return Browser("chrome", **executable_path, headless=False)


# def scrape():
#     browser = init_browser()
#     url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
#     browser.visit(url)
#     browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')

#     html = browser.html
#     soup = BeautifulSoup(html, 'html.parser')

#     image=soup.find_all('img')[5]['src']
#     img_img = ("https://astrogeology.usgs.gov"+image)   

#     hemisphere_image_urls = [
#     # # {"title": "Valles Marineris Hemisphere", "img_url": tiff_path},
#     {"title": "Cerberus Hemisphere", "img_url": img_img}
#     # # {"title": "Schiaparelli Hemisphere", "img_url": img_pathway},
#     # # {"title": "Syrtis Major Hemisphere", "img_url": image_path},
#     ]
#     return img_img