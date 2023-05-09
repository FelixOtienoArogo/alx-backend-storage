"""schools_by_topic"""
def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    return [school for school in mongo_collection.find({"topics": topic})]
