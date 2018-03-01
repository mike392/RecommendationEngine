'''
Created on Jul 14, 2017

@author: Mikhail_Barsukou
'''
import datetime

def get_mongo_collection(db_instance, collection_name):
        return db_instance.get_collection(name=collection_name) if collection_name in db_instance.collection_names() else None
    
def insert_data_to_collection(db_instance, collection, object):
        id = collection.insert(object)
        insert_session(db_instance, id, collection.name)
        #print "1"
        
def get_data_from_collection(collection):
        return collection.find()
    
def insert_session(db_instance, id, collection_name):
        now = datetime.datetime.now()
        index = get_next_session_index(db_instance, collection_name)
        result = {'SessionIndex' : index, 'SessionTime': str(now), 'SessionId' : str(id),  'CollectionName': collection_name}
        db_instance.sessions.insert(result)
        
def get_next_session_index(db_instance, collection_name):
        result = get_max_session_index(db_instance, collection_name)
        return (result + 1) if result else 1
    
def get_max_session_index(db_instance, collection_name):
        result = list(db_instance.sessions.aggregate([{
            '$match' : { 'CollectionName' : collection_name}
            },
            {'$group' : { '_id': 0, 'count' : { '$max' : '$SessionIndex'} }}]))
        return result[0]['count'] if len(result) > 0 else None
    
def get_last_session_id(db_instance, collection_name):
        result = list(db_instance.sessions.find({'SessionIndex' : get_max_session_index(db_instance, collection_name)}))
        return result[0]['SessionId']