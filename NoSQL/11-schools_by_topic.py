#!/usr/bin/env python3
"""Looking for school with a written topic."""
def schools_by_topic(mongo_collection, topic):
    """This fucntion dearches for schools that has a specific topic."""
    return mongo_collection.find({"topics": {"$in": [topic]}})
