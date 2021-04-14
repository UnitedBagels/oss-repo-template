from pymongo import MongoClient
from bson.objectid import ObjectId
import pprint
import random
import datetime
client = MongoClient()


def random_word_requester():
    '''
    This function should return a random word and its definition and also
    log in the MongoDB database the timestamp that it was accessed.
    '''

    doc_num = random.randrange(definitions.estimated_document_count())

    count = 0
    for doc in definitions.find():
        if count == doc_num:
            date = datetime.datetime.utcnow().isoformat()
            obj = ObjectId(str(doc["_id"]))
            try:
                date_list = doc['dates']
                date_list.append(date)
                definitions.update_one({'_id': obj}, {'$set': {'dates': date_list}})

            except KeyError:
                definitions.update_one({'_id': obj}, {'$set': {'dates': [date]}})

            return definitions.find_one({'_id': obj})

        count += 1

    return


if __name__ == '__main__':

    client = MongoClient('mongodb://localhost:27018/')

    db = client.mongo_db_lab

    definitions = db.definitions

    print(random_word_requester())
