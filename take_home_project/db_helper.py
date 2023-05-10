#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Vaishnavi Chilakamarthi
# Created Date: Mon May 1 16:00:00 EST 2023
# =============================================================================
"""This is the Database Helper class to enable 
connection and data access from the Database."""
# =============================================================================
# Imports
# =============================================================================

import os
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
import pandas as pd


class Db_helper:
    def __init__(self) -> None:
        # Fetching environment variables
        self.hostStr = os.getenv("POSTGRES_HOST")
        self.dbPort = os.getenv("POSTGRES_PORT")
        self.dbStr = os.getenv("POSTGRES_DB")
        self.uNameStr = os.getenv("POSTGRES_USER")
        self.dbPassStr = os.getenv("POSTGRES_PASSWORD")

        # Creating the URI to access the postges database
        self.db_uri = (
            "postgresql://"
            + self.uNameStr
            + ":"
            + self.dbPassStr
            + "@"
            + self.hostStr
            + ":"
            + self.dbPort
            + "/"
            + self.dbStr
        )

        # Create the database engine
        self.eng = db.create_engine(self.db_uri)

        # Establishing session with the database
        self.session = sessionmaker(bind=self.eng)()

    # Function to fetch data from the database tables based on teh Object
    def fetch_data(self, Object: any) -> pd.DataFrame:
        # Initializing empty list to store values fetched from teh databse
        self.data_list = []
        self.fetched_values = self.session.query(
            Object
        )  # Executing the query and fetching the data

        # Iterating through the fetched values and appending to the data list
        for i in self.fetched_values:
            self.data_list.append([i.time, i.value])

        # Creating a dataframe out of the data_list
        df=pd.DataFrame(self.data_list, columns=["Time", "Value"])

        # Converting the type of the Time column to datetime from object
        df["Time"]=pd.to_datetime(df["Time"])

        # Returning a dataframe
        return df
