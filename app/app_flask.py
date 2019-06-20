import os
from flask import Flask, render_template, jsonify, request, redirect, Response
from flask_sqlalchemy import SQLAlchemy
from app.extensions import db
from app import config, data_models
import pandas as pd

# app = Flask(__name__)


# ################################################
# Database Setup
# ################################################



# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(db.engine, reflect=True)

# # Save references to each of the tables
# Samples_Metadata = Base.classes.sample_metadata
# Samples = Base.classes.samples

def buildApp():
    # Flask "app" Setup
    flask_app = Flask(__name__)
    
# app.config["chicago_neighborhoods_db"] = DATABASE_URL
    db = SQLAlchemy(flask_app)
    # *********************************************
    # ************** Database Setup ***************
    # *********************************************
    # Check for enviroment variable DATABASE_URL
    # If it doesn't exist use DATABASE_URL from config.py

    flask_app.config['chicago_neighborhoods_db'] = os.environ.get('DATABASE_URL', '') or config.DATABASE_URL
    flask_app.config['chicago_neighborhoods_db'] = False

    # Attach db to Flask app so Flask handels db session managment and other good things
    db.init_app(flask_app)
    # Create database tables based on the model definitions in data_models.py
    db.create_all(app=flask_app)


# Routes for webpages

    @flask_app.route("/")
    def renderHome():
        return render_template("index.html")


# Routes for data
    @flask_app.route("/api/asian")
    def getAsianData():
        df = pd.read_sql("""
        select  * from    asian_data""", db.engine)
        asian_file = df.to_csv()
        return asian_file
#coffe data
    @flask_app.route("/api/coffee")
    def getCoffeeData():
        df = pd.read_sql("""select  * from    coffee_data""", db.engine)
        coffee_file = df.to_csv()
        return coffee_file
#ghost data
    @flask_app.route("/api/ghost")
    def getGhostData():
        df = pd.read_sql("""
        select  * 
        from    haunted_data
        """, db.engine)
        ghost_file = df.to_csv()
        return ghost_file
#library data
    @flask_app.route("/api/library")
    def getLibraryData():
        df = pd.read_sql("""
        select  * 
        from    library_data
        """, db.engine)
        library_file = df.to_csv()
        return library_file
#Mexican data
    @flask_app.route("/api/mexican")
    def getMexicanData():
        df = pd.read_sql("""
        select  * 
        from    mexican_data
        """, db.engine)
        mexican_file = df.to_csv()
        return mexican_file
#pizza data
    @flask_app.route("/api/pizza")
    def getPizzaData():
        df = pd.read_sql("""
        select  * 
        from    pizza_data
        """, db.engine)
        pizza_file = df.to_csv()
        return pizza_file
#redlight data
    @flask_app.route("/api/redlight")
    def getRedlightData():
        df = pd.read_sql("""
        select  * 
        from    redlight_data
        """, db.engine)
        redlight_file = df.to_csv()
        return redlight_file
    return flask_app
if __name__ == "__main__":
    app.run()

debug=True
