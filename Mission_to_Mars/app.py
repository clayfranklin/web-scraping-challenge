from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/marsy"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/marsy")


@app.route("/")
def index():
    hemisphere_img_urls = mongo.db.mars.find_one()
    return render_template("index.html", hemisphere_img_urls=hemisphere_img_urls)


@app.route("/scrape")
def scraper():
    marsy = mongo.db.marsy
    marsy_data = scrape_mars.scrape()
    marsy.update({}, marsy_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)