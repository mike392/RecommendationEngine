# -*- coding: utf-8 -*-
'''
Created on Jul 14, 2017

@author: Mikhail_Barsukou
'''
import unittest
from driver.MongoDriver import MongoDriver
from util.MongoUtils import *
from util.IdGenerator import IdGenerator
from service.DataStub import *
import json
import os
import util.Constants as const
import random
from stubutils.StubUtils import *
from service.DataPreparationHandler import get_data
from util.PandasUtils import PandasUtils
from pprint import PrettyPrinter
from util.DataPreparationUtils import *
from util import JsonUtils
import pandas as pd
from service.Predictor import Predictor
import xgboost as xgb
from sklearn.metrics import accuracy_score
import DisplayHelper
from DisplayHelper import *

class MongoDriverTest(unittest.TestCase):

#     def test_get_database(self):
#         mongo_driver = MongoDriver.get_instance()
#         db_instance = mongo_driver.get_db_instance(database_name="BigDataABW", host="185.66.69.113", port=27017)
#         self.assertIsNotNone(db_instance, "database not found")      
#         
#     def test_get_database_collections(self):
#         mongo_driver = MongoDriver.get_instance()
#         db_instance = mongo_driver.get_db_instance(database_name="BigDataABW", host="185.66.69.113", port=27017)
#         collection = MongoUtils.get_mongo_collection(db_instance, "RawData")
#         self.assertIsNotNone(collection, "collection in database not found") 
#         
#     def test_id_generator(self):
#         for i in range(1,10):
#             print(IdGenerator.get_instance().get_id())
#             
#     def test_data_stub(self):
#         for i in range(1,10):
#             print(DataStub.generate_data())
#             
#     def test_insert_generated_data(self):
#         result = []
#         for i in range(1,10):
#             result.append(DataStub.generate_data())
#         self.assertIsNotNone(result, "No data generated")
#         mongo_driver = MongoDriver.get_instance()
#         db_instance = mongo_driver.get_db_instance(database_name="BigDataABW", host="185.66.69.113", port=27017)
#         collection = MongoUtils.get_mongo_collection(db_instance, "RawData")
#         #collection.remove()
#         MongoUtils.insert_data_to_collection(collection, result)
#         
#     def test_select_data_from_collection(self):
#         mongo_driver = MongoDriver.get_instance()
#         db_instance = mongo_driver.get_db_instance(database_name="BigDataABW", host="185.66.69.113", port=27017)
#         collection = MongoUtils.get_mongo_collection(db_instance, "RawData")
#         result = MongoUtils.get_data_from_collection(collection)
#         self.assertIsNotNone(result, "No data were selected")
#         for item in result:
#             print item
            
    def test_data_generation(self):
        db_instance = MongoDriver.get_instance().get_db_instance(const.DB_INSTANCE)
        collection = get_mongo_collection(db_instance, "normalized_data")
        generate_and_insert_data(db_instance, collection)

#     def test_data_retrieval(self):
#         db_instance = MongoDriver.get_instance().get_db_instance(const.DB_INSTANCE)
#         data = get_data(db_instance, 'normalized_data')
#         df = PandasUtils.get_dataframe(data, const.JSON_STRUCTURE)
#         
#         print "1"
        
#         
#     def test_dataframe_creation(self):
#         db_instance = MongoDriver.get_instance().get_db_instance(const.DB_INSTANCE)
#         data = get_data(db_instance, 'normalized_data')
#         dataframe = PandasUtils.get_dataframe(data, const.JSON_STRUCTURE)
#         printer = PrettyPrinter()
#         printer.pprint(dataframe)

#     def test_json_update(self):
#         data = open_file(const.MODELS_JSON_ROUTE)
#         result_list = []
#         for idx, item in enumerate(data['tree']):
#             result = {}
#             result['id'] = idx+1
#             result['name'] = item['name']
#             result['children'] = []
#             for idx, inner_item in enumerate(item['children']):
#                 result['children'].append({ idx+1 : inner_item})
#                 print inner_item
#             result_list.append(result)
#         with open(os.path.join(os.path.dirname(__file__), const.MODELS_ID_MAPPING_JSON_ROUTE), 'w') as fp:
#             json.dump(result_list, fp)
            
#     def test_json_data_update(self):
#         JsonUtils.body_transmission_wheel_json_update()

#     def test_get_dataset(self):
#         df = DatasetHolder.get_instance().get_dataset()

#     def test_training_and_prediction(self):
#         Predictor.get_instance().train_model()

#     def test_percentiles(self):
#         df = DatasetHolder.get_instance().get_dataset()
#         df = process_delta_columns(df)
#         for column in const.NUMERIC_COLUMNS_REQUIRE_ANALYSIS:
#             percentiles = get_percentiles_for_numeric_column(df, column)
#     def test_date_conversion(self):
#         df = DatasetHolder.get_instance().get_dataset()
#         df = process_data_ids(df)
#         df = process_delta_columns(df)
#         df = process_numeric_columns(df)
#         df = process_date_columns(df)
#         df = drop_unhandled_columns(df)
#         X_data = df.drop("search_marka", axis=1)          # data: Features
#         Y_data = df["search_marka"]                       # data: Labels
# 
#         X_train, X_test, Y_train, Y_test = train_test_split(X_data, Y_data, test_size=0.2, random_state=0)
#         X_train = X_train.drop('user_id', axis=1)
# 
#         X_test_ref = X_test.drop('user_id', axis=1)
#         xg_train = xgb.DMatrix(X_train, label=Y_train)
#         xg_test = xgb.DMatrix(X_test_ref, label=Y_test)
#         # setup parameters for xgboost
#         param = {}
#         # use softmax multi-class classification
#         param['objective'] = 'multi:softmax'
#         # scale weight of positive examples
#         param['eta'] = 0.1
#         param['max_depth'] = 6
#         param['silent'] = 1
#         param['nthread'] = 4
#         param['num_class'] = 200
#         watchlist = [(xg_train, 'train'), (xg_test, 'test')]
#         num_round = 155
#         bst = xgb.train(param, xg_train, num_round, watchlist)
#         # get prediction
#         Y_pred  = bst.predict(xg_test)
#         
#         print('Accuracy score = {}'.format(accuracy_score(Y_test, Y_pred)))


        
def suite(self):  
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(MongoDriverTest))
    return suite

if __name__=='__main__':
    unittest.main()

