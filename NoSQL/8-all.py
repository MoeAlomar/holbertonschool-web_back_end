#!/usr/bin/env python3
"""
Module 8-all
Function to list all documents in a MongoDB collection
"""

def list_all(mongo_collection):
    """
    Lists all documents in a collection.
    Args:
        mongo_collection: pymongo collection object
    Returns:
        list of documents, or empty list if none
    """
    return list(mongo_collection.find())