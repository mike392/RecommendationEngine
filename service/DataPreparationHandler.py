'''
Created on Jul 17, 2017

@author: Mikhail_Barsukou
'''
from util.MongoUtils import get_last_session_id
from bson.objectid import ObjectId
import util.Constants as const
from driver.MongoDriver import MongoDriver
from util.PandasUtils import PandasUtils
from util.DataPreparationUtils import *
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import Imputer , Normalizer , scale, LabelEncoder
from service.DatasetHolder import DatasetHolder
import pandas as pd
from datetime import datetime

def get_data(db_instance, collection_name):
        session_id = get_last_session_id(db_instance, collection_name)
        result = list(db_instance[collection_name].aggregate([{'$match':{'_id' : ObjectId(session_id)}
    },
    {
    '$unwind': {'path' : '$ABWData'}
    }, 
    {
        '$project' : {
            '_id':0,
            'search_engine' : '$ABWData.search_engine',
            'search_marka' : '$ABWData.search_marka',
            'user_id' : '$ABWData.user_id',
            'search_model' : '$ABWData.search_model',
            'search_city' : '$ABWData.search_city',
            'search_milleage_to' : '$ABWData.search_milleage_to',
            'search_body' : '$ABWData.search_body',
            'search_price_from' : '$ABWData.search_price_from',
            'search_year_from' : '$ABWData.search_year_from',
            'search_condition' : '$ABWData.search_condition',
            'search_country' : '$ABWData.search_country',
            'search_year_to' : '$ABWData.search_year_to',
            'last_login' : '$ABWData.last_login',
            'search_price_to' : '$ABWData.search_price_to',
            'search_volume_from' : '$ABWData.search_volume_from',
            'search_text' : '$ABWData.search_text',
            'search_transmission' : '$ABWData.search_transmission',
            'search_wheel' : '$ABWData.search_wheel',
            'search_rigion' : '$ABWData.search_rigion',
            'search_milleage_from' : '$ABWData.search_milleage_from',
            'search_volume_to' : '$ABWData.search_volume_to'
            }
     },
                                                           { '$limit' : const.ROWS_NUMBER_LIMIT}]))
        return result
    
def get_prepared_data_for_target(target_column_name):
    dataframe = pd.DataFrame(DatasetHolder.get_instance().get_dataset())
    dataframe = process_data(dataframe)
    X_data = dataframe.drop(target_column_name, axis=1)          # data: Features
    Y_data = dataframe[target_column_name]                       # data: Labels
#     #avoid objects in columns
#     for f in X_data.columns: 
#         if X_data[f].dtype=='object': 
#             lbl = LabelEncoder() 
#             lbl.fit(list(X_data[f].values)) 
#             X_data[f] = lbl.transform(list(X_data[f].values))
    #split data into random "train" and "test" set 
    #X_train, X_test, Y_train, Y_test = train_test_split(X_data, Y_data, test_size=0.2, random_state=0)
    return train_test_split(X_data, Y_data, test_size=0.2, random_state=0)

def process_data(dataframe):
    d1 = datetime.now()
    dataframe = process_data_ids(dataframe)
    d2 = datetime.now()
    delta = d2 - d1
    print ('Process ids finished in {} seconds'.format(delta.seconds))
    dataframe = process_delta_columns(dataframe)
    d3 = datetime.now()
    delta = d3 - d2
    print ('Process delta columns finished in {} seconds'.format(delta.seconds))
    #Drop unhandled columns
    for column in const.COLUMNS_TO_DROP:
        dataframe = dataframe.drop(column, axis=1)
    #avoid objects in values
    for f in dataframe.columns: 
        if dataframe[f].dtype=='object': 
            lbl = LabelEncoder() 
            lbl.fit(list(dataframe[f].values)) 
            dataframe[f] = lbl.transform(list(dataframe[f].values))
    #Numeric representation for column
    for column in const.NUMERIC_COLUMNS_REQUIRE_ANALYSIS:
        quartiles = get_percentiles_for_numeric_column(dataframe,column)[0]
        dataframe.loc[ dataframe[column] <= quartiles['values'][1], column] = 0
        dataframe.loc[(dataframe[column] > quartiles['values'][1]) & (dataframe[column] <= quartiles['values'][2]), column] = 1
        dataframe.loc[(dataframe[column] > quartiles['values'][2]) & (dataframe[column] <= quartiles['values'][3]), column]   = 2
        dataframe.loc[ dataframe[column] > quartiles['values'][3], column] = 3
        dataframe[column] = dataframe[column].astype(int)
    d4 = datetime.now()
    delta = d4 - d3
    print ('Process numeric columns finished in {} seconds'.format(delta.seconds))
    return dataframe

