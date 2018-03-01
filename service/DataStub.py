'''
Created on Jul 14, 2017

@author: Mikhail_Barsukou
'''
from util import Constants
from util.IdGenerator import IdGenerator
from datetime import datetime
from stubutils.StubUtils import *
from util.MongoUtils import *

def generate_data_record():
        result = {}
        result[Constants.JSON_STRUCTURE[20]] = IdGenerator.get_instance().get_id()
        result[Constants.JSON_STRUCTURE[0]] = get_random_date()
        result[Constants.JSON_STRUCTURE[6]] = get_random_model()
        result[Constants.JSON_STRUCTURE[9]] = get_random_make(result[Constants.JSON_STRUCTURE[6]])
        result[Constants.JSON_STRUCTURE[15]] = get_random_volume_from()
        result[Constants.JSON_STRUCTURE[16]] = get_random_volume_to(result[Constants.JSON_STRUCTURE[15]])
        result[Constants.JSON_STRUCTURE[14]] = get_random_transmission()
        result[Constants.JSON_STRUCTURE[7]] = get_random_milleage_from()
        result[Constants.JSON_STRUCTURE[8]] = get_random_milleage_to(result[Constants.JSON_STRUCTURE[7]])
        result[Constants.JSON_STRUCTURE[4]] = get_random_country()
        result[Constants.JSON_STRUCTURE[12]] = get_random_region(result[Constants.JSON_STRUCTURE[4]])
        result[Constants.JSON_STRUCTURE[2]] = get_random_city(result[Constants.JSON_STRUCTURE[4]],result[Constants.JSON_STRUCTURE[12]])
        result[Constants.JSON_STRUCTURE[3]] = "search_condition"
        result[Constants.JSON_STRUCTURE[13]] = "search_text"
        result[Constants.JSON_STRUCTURE[17]] = get_random_wheel()
        result[Constants.JSON_STRUCTURE[18]] = get_random_year_from()
        result[Constants.JSON_STRUCTURE[19]] = get_random_year_to(result[Constants.JSON_STRUCTURE[18]])
        result[Constants.JSON_STRUCTURE[5]] = "engine"
        result[Constants.JSON_STRUCTURE[1]] = get_random_body()
        result[Constants.JSON_STRUCTURE[10]] = get_random_price_from()
        result[Constants.JSON_STRUCTURE[11]] = get_random_price_to(result[Constants.JSON_STRUCTURE[10]])
        return result
    
def generate_and_insert_data(db_instance, collection):
        result = {}
        initial_result = []
        for i in range(1, 10000):
            record = generate_data_record()
            initial_result.append(record)  
        result["ABWData"] = initial_result
        insert_data_to_collection(db_instance, collection, result)