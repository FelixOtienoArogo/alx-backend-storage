#!/usr/bin/env python3
"""MongoDB Find"""


def schools_by_topic(mongo_collection, topic):
    """
    Use an aggregate to find documents
    :param mongo_collection: Pymongo connection
    :param topic: The topic to search
    :return: The list of school that having the same topics
    """
    return [school for school in mongo_collection.find({"topics": topic})]
