#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By  : Vaishnavi Chilakamarthi
# Created Date: Mon May 1 16:00:00 EST 2023
# =============================================================================
"""This is the models package that describe 
all the ORM classes required to map the 
data fetched from the Database"""
# =============================================================================
# Imports
# =============================================================================

import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


"""Creating a model class for values in Stock1_Price table"""


class Stock1_Price(Base):
    __tablename__ = "stock1_price"
    time = db.Column(db.DateTime, primary_key=True)
    value = db.Column(db.BigInteger)


"""Creating a model class for values in Stock2_Price table"""


class Stock2_Price(Base):
    __tablename__ = "stock2_price"
    time = db.Column(db.DateTime, primary_key=True)
    value = db.Column(db.BigInteger)


"""Creating a model class for values in Stock3_Price table"""


class Stock3_Price(Base):
    __tablename__ = "stock3_price"
    time = db.Column(db.DateTime, primary_key=True)
    value = db.Column(db.BigInteger)


"""Creating a model class for values in Stock4_Price table"""


class Stock4_Price(Base):
    __tablename__ = "stock4_price"
    time = db.Column(db.DateTime, primary_key=True)
    value = db.Column(db.BigInteger)
