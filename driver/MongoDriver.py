'''
Created on Jul 14, 2017

@author: Mikhail_Barsukou
'''
import pymongo
import util.Constants as const


class MongoDriver(object):
    '''
    classdocs
    '''
    __instance = None
    @staticmethod
    def get_instance():
        if not MongoDriver.__instance:
            MongoDriver.__instance = MongoDriver(const.HOST, const.PORT)
        return MongoDriver.__instance
    
    def __init__(self, host, port):
        self.host = host
        self.port = port
        print ("Constructor called")
        
    def get_db_instance(self, database_name):
        client = pymongo.MongoClient(host=self.host, port=self.port)
        db_names_list = client.database_names()
        db = client.get_database(name=database_name) if database_name in db_names_list else None
        return db
    
    