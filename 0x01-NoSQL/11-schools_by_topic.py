#!/usr/bin/env python3
"""List schools by topic"""


def schools_by_topic(mongo_collection, topic):
    """List schools by topic class""" 
    mongo_collection.find({"topics": topic})