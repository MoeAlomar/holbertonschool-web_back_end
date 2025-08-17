#!/usr/bin/env python3
"""
Module 9-insert_school
Function to insert a new document in a collection
"""
def insert_school(mongo_collection, **kwargs):
    """ Inserting a new doc in the collection and returning its id."""


    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
