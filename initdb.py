run_script = input("\nAre you sure you want to run this script? (Y)es or (N)o\nWARNING: If you have an existing database, it will be deleted\n\n> ")
if "y" not in run_script.lower():
    exit(0)

import os
import pandas as pd
# Import database settings from flask_app file
from app import flask_app
from app.extensions import db

# This "with" allows us to borrow our db setting and data models from the flask app
with flask_app.app_context():

    print("Delete existing tables")
    db.drop_all()
    # Create database tables based on the model definitions in data_models.py
    print("Creating new tables based on data model")
    db.create_all()

    # Import a csv file into a pandas dataframe, clean, then save the results to a database table
    path_for_this_file = os.path.dirname(__file__)
    file_name = "asianUpdate.csv"
    absolute_csv_path = os.path.join(path_for_this_file, "Datasets", file_name)
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
    absolute_csv_path = os.path.join(path_for_this_file, "Datasets", file_name)
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