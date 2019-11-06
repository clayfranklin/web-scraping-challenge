import pandas as pd

def facts():
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)

    df2=tables[1]
    df2 = df2.drop(columns=['Earth'])
    df2.columns = ['Attribute', 'Mars']


    df=tables[0]
    df.columns = ['Attribute', 'Mars']
    df = pd.DataFrame(df)   
    
    df_mars = pd.concat([df, df2])

    df_mars.reset_index([])
    df_2=df_mars.set_index('Attribute')
    mars_fact = df_2.drop([df_2.index[0], df_2.index[1] , df_2.index[2]])

    return mars_fact



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