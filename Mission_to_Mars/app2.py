import hemiscrape
import fact
import weather
import featured
import news
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")



# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/marsy")

@app.route("/")
def index():
    mars_data = mongo.db.collection.find_one()
    #add thing to put my table in here
    return render_template("index.html", mars_data=mars_data)

 
@app.route("/scrape")
def scraper():
    feat_img = featured.img_finder()
    feat_news = news.news_scrape()
    mars_weather = weather.weather_scraper()
    facts = fact.fact_scrape()
    img_urls = hemiscrape.scrape()
    mongo.db.collection.remove({})
    mongo.db.collection.insert(
        {
        'weather': mars_weather,
        'url': img_urls, 
        'facts': facts, 
        'img': feat_img,
        'news': feat_news
        }
        )
   
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)