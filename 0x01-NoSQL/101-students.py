#!/usr/bin/env pyhton3
"""top_students"""

def top_students(mongo_collection):
    """returns all students sorted by average score"""
    top = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg":  "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])
    return top
