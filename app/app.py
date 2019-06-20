import os
import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from db_config import DATABASE_URL

app = Flask(__name__)


#################################################
# Database Setup
#################################################

app.config["chicago_neighborhoods_db"] = DATABASE_URL
db = SQLAlchemy(app)

# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(db.engine, reflect=True)

# # Save references to each of the tables
# Samples_Metadata = Base.classes.sample_metadata
# Samples = Base.classes.samples



# Routes for webpages

@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


# Routes for data
#asian restaurant data
@app.route("/api/asian")
def getAsianData():
    df = pd.read_sql("""
        select  * 
        from    asian_data
        """, db.engine)
    asian_file = df.to_csv()
    return asian_file
#coffe data
@app.route("/api/coffee")
def getCoffeeData():
    df = pd.read_sql("""
        select  * 
        from    coffee_data
        """, db.engine)
    coffee_file = df.to_csv()
    return coffee_file
#ghost data
@app.route("/api/ghost")
def getGhostData():
    df = pd.read_sql("""
        select  * 
        from    haunted_data
        """, db.engine)
    ghost_file = df.to_csv()
    return ghost_file
#library data
@app.route("/api/library")
def getLibraryData():
    df = pd.read_sql("""
        select  * 
        from    library_data
        """, db.engine)
    library_file = df.to_csv()
    return library_file
#Mexican data
@app.route("/api/mexican")
def getMexicanData():
    df = pd.read_sql("""
        select  * 
        from    mexican_data
        """, db.engine)
    mexican_file = df.to_csv()
    return mexican_file
#pizza data
@app.route("/api/pizza")
def getPizzaData():
    df = pd.read_sql("""
        select  * 
        from    pizza_data
        """, db.engine)
    pizza_file = df.to_csv()
    return pizza_file
#redlight data
@app.route("/api/redlight")
def getRedlightData():
    df = pd.read_sql("""
        select  * 
        from    redlight_data
        """, db.engine)
    redlight_file = df.to_csv()
    return redlight_file
if __name__ == "__main__":
    app.run()
