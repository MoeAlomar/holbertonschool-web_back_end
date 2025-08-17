#!/usr/bin/env python3
""" this module updates the topics of
a specific school name in the collection."""

def update_topics(mongo_collection, name, topics):
        """
    Collection: argv[1]
    Document model: { "name": <str>, "topics": [<str>] }

    Update all documents with the given name,
    setting their topics field to the provided list.
    """
    mongo_collection.update_one(
        {"name": name}, { "$set": {"topics": topics} })
