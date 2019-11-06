from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import hemiscrape

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/marsy"
mongo = PyMongo(app)



# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/marsy")

@app.route("/")
def index():
    hemisphere_img_urls = mongo.db.marsy.find_one()
    return render_template("index.html", hemisphere_img_urls=hemisphere_img_urls)


@app.route("/scrape")
def scraper():
    marsy = mongo.db.marsy
    marsy_data = hemiscrape.scrape()
    # marsy.update({}, marsy_data, upsert=True)
    marsy.insert({'url': marsy_data})
    return redirect(marsy_data, code=302)


if __name__ == "__main__":
    app.run(debug=True)