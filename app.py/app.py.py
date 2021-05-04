#Import Dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scrape
import os


#Create flask app
app = Flask(__name__)   

#Use flask_pymongo to set up mongo connection
app.config["Mongo_URL"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#Create route that renders index.html template & find documents 
@app.route("/")

def home():

        #obtain data
        mars_information = mongo.db.mars_information.find_one()
        return render_template("index.html", mars_information=mars_information)

#Create route for scrape function
@app.route("/scrape")
def scrape():

        #scrape functions
        mars_information = mongo.db.mars_information
        mars_data = mars_scrape.mars_scrape_news()
        mars_data = mars_scrape.mars_scrape_mars_image()
        mars_fact = mars_scrape.scrape_mars_facts()
        scrape_mars_hemisphere= scrape_mars.scrape_mars_hemispheres()
        mars_info.update({}, mars_data, upsert=True)

        return redirect("/", code=302)

    if __name__ =="__main__":
        app.run(debug=True)