from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import hemiscrape
import fact

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
    # marsy = mongo.db.marsy
    # marsy_data = hemiscrape.scrape()
    facts = fact.facts().to_dict() 
    # # marsy.update({}, marsy_data , upsert=True)
    # marsy.insert({'url': marsy_data, 'facts': facts})
    # # marsy.insert({'url': mars_fact })
    img_urls = hemiscrape.scrape()
    # mars_data.insert({'url': img_urls, 'facts' : facts})
    mongo.db.collection.insert({'url': img_urls, 'facts': facts})
    
    
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)