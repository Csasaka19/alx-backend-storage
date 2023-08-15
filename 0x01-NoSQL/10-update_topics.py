#!/usr/bin/env python3
"""Changes topic of a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """Update topics class"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})