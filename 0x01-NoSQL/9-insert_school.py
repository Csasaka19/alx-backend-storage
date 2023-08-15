#!/usr/bin/env python3
"""Insert a document in Mongodb using Python
based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """Insert a document class"""
    final = mongo_collection.insert_one(kwargs)
    return final.inserted_id