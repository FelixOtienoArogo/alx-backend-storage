"""8-all."""
def list_all(mongo_collection):
    """
    Description.

    --------------
    function that lists all documents in a collection
    """
    doc_list  = []
    
    document = mongo_collection.find()

    for doc in document:
        doc_list.append(doc)
    return doc_list
