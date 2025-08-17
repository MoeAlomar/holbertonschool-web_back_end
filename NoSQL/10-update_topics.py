#!/usr/bin/env python3
def update_topics(mongo_collection, name, topics):
    """
    Update all topics of a school document by name.

    Collection: school
    Document model: { "name": <str>, "topics": [<str>] }

    Args:
        mongo_collection: pymongo collection object
        name (str): school name to update
        topics (list[str]): new topics list
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
