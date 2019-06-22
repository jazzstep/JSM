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

    # Flask "app" Setup
app = Flask(__name__)
    
# app.config["chicago_neighborhoods_db"] = DATABASE_URL
    
    # *********************************************
    # ************** Database Setup ***************
    # *********************************************
    # Check for enviroment variable DATABASE_URL
    # If it doesn't exist use DATABASE_URL from config.py

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or config.DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    

# Attach db to Flask app so Flask handels db session managment and other good things
db.init_app(app)
# Create database tables based on the model definitions in data_models.py

# Routes for webpages

@app.before_first_request
def loadCsvData():
    # Import a csv file into a pandas dataframe, clean, then save the results to a database table
    path_for_this_file = os.path.dirname(__file__)
    file_name = "asianUpdate.csv"
    absolute_csv_path = os.path.join(path_for_this_file, ".." ,"Datasets", file_name)
    db_table_name = "asian_table"

    print(f"Importing csv {'asianUpdate'}")
    df = pd.read_csv(absolute_csv_path)

    # print("\nClean and transform ....\n")
    # # CLEAN
    # # TRANSFORM
    print(df.head())

    print(f"Saving results to {'asian_data'}")
    # Save results from import as 
    df.to_sql(db_table_name, con=db.engine, if_exists="replace", chunksize=20000)
    print("DONE!")

    #-----------------------------------------------------------#
        # Import a csv file into a pandas dataframe, clean, then save the results to a database table
    path_for_this_file = os.path.dirname(__file__)
    file_name = "coffeeUpdate.csv"
    absolute_csv_path = os.path.join(path_for_this_file, ".." , "Datasets", file_name)
    db_table_name = "coffee_table"

    print(f"Importing csv {'coffeeUpdate'}")
    df = pd.read_csv(absolute_csv_path)

    # print("\nClean and transform ....\n")
    # # CLEAN
    # # TRANSFORM
    # print(df.head())

    print(f"Saving results to {'coffee_data'}")
    # Save results from import as 
    df.to_sql(db_table_name, con=db.engine, if_exists="replace", chunksize=20000)
    print("DONE!")
    #-----------------------------------------------------------#
        # Import a csv file into a pandas dataframe, clean, then save the results to a database table
    path_for_this_file = os.path.dirname(__file__)
    file_name = "CPLdata1.csv"
    absolute_csv_path = os.path.join(path_for_this_file, "Datasets", file_name)
    db_table_name = "library_data"

    print(f"Importing csv {'CPLdata1'}")
    df = pd.read_csv(absolute_csv_path)

    # print("\nClean and transform ....\n")
    # # CLEAN
    # # TRANSFORM
    # print(df.head())

    print(f"Saving results to {'library_data'}")
    # Save results from import as 
    df.to_sql(db_table_name, con=db.engine, if_exists="replace", chunksize=20000)
    print("DONE!")
        #-----------------------------------------------------------#
        # Import a csv file into a pandas dataframe, clean, then save the results to a database table
    path_for_this_file = os.path.dirname(__file__)
    file_name = "hauntedUpdate.csv"
    absolute_csv_path = os.path.join(path_for_this_file, "Datasets", file_name)
    db_table_name = "haunted_data"

    print(f"Importing csv {'haunted'}")
    df = pd.read_csv(absolute_csv_path)

    # print("\nClean and transform ....\n")
    # # CLEAN
    # # TRANSFORM
    # print(df.head())

    print(f"Saving results to {'haunted_data'}")
    # Save results from import as 
    df.to_sql(db_table_name, con=db.engine, if_exists="replace", chunksize=20000)
    print("DONE!")
            #-----------------------------------------------------------#
        # Import a csv file into a pandas dataframe, clean, then save the results to a database table
    path_for_this_file = os.path.dirname(__file__)
    file_name = "mexicanUpdate.csv"
    absolute_csv_path = os.path.join(path_for_this_file, "Datasets", file_name)
    db_table_name = "mexican_data"

    print(f"Importing csv {'mexican'}")
    df = pd.read_csv(absolute_csv_path)

    # print("\nClean and transform ....\n")
    # # CLEAN
    # # TRANSFORM
    # print(df.head())

    print(f"Saving results to {'mexican_data'}")
    # Save results from import as 
    df.to_sql(db_table_name, con=db.engine, if_exists="replace", chunksize=20000)
    print("DONE!")
                #-----------------------------------------------------------#
        # Import a csv file into a pandas dataframe, clean, then save the results to a database table
    path_for_this_file = os.path.dirname(__file__)
    file_name = "pizzaUpdate.csv"
    absolute_csv_path = os.path.join(path_for_this_file, "Datasets", file_name)
    db_table_name = "pizza_data"

    print(f"Importing csv {'pizza'}")
    df = pd.read_csv(absolute_csv_path)

    # print("\nClean and transform ....\n")
    # # CLEAN
    # # TRANSFORM
    # print(df.head())

    print(f"Saving results to {'pizza_data'}")
    # Save results from import as 
    df.to_sql(db_table_name, con=db.engine, if_exists="replace", chunksize=20000)
    print("DONE!")
                    #-----------------------------------------------------------#
        # Import a csv file into a pandas dataframe, clean, then save the results to a database table
    path_for_this_file = os.path.dirname(__file__)
    file_name = "red-light-camera-locations.csv"
    absolute_csv_path = os.path.join(path_for_this_file, "Datasets", file_name)
    db_table_name = "redlight_data"

    print(f"Importing csv {'redlight'}")
    df = pd.read_csv(absolute_csv_path)

    # print("\nClean and transform ....\n")
    # # CLEAN
    # # TRANSFORM
    # print(df.head())

    print(f"Saving results to {'redlight_data'}")
    # Save results from import as 
    df.to_sql(db_table_name, con=db.engine, if_exists="replace", chunksize=20000)
    print("DONE!")

@app.route("/")
def renderHome():
    return render_template("index.html")


# Routes for data
@app.route("/api/asian")
def getAsianData():
    df = pd.read_sql("""
    select  * from    asian_table""", db.engine)
    asian_file = df.to_csv()
    return asian_file
#coffe data
@app.route("/api/coffee")
def getCoffeeData():
    df = pd.read_sql("""select  * from    coffee_table""", db.engine)
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

#Library info
@app.route("/api/library/count/${neighborhood_name}")
def getLibraryCount():
    library_count = pd.read_sql("""
    select  COUNT(*)
    FROM    library_data
    WHERE   Neighborhood = '${neighborhood_name}'
    """, db.engine)
    return library_count
        

