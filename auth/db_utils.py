from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['microservices-course']
collection = db.messages

def get_all_messages():
    cursor = collection.find()
    return list(cursor)

def get_message(id):
    result = collection.find_one({'_id': id})
    return result

def add_message(data):
    id = collection.insert_one(data)
    return id

def edit_message(id, data):
    result = collection.update_one({'_id': id}, 
        {'$set': data})
    return str(result.modified_count) 
