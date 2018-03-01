'''
Created on Jul 18, 2017

@author: Mikhail_Barsukou
'''
from stubutils.StubUtils import open_file
import util.Constants as const
from service.QuartileHolder import QuartileHolder
from service.DatasetHolder import DatasetHolder
from service.DataPreparationHandler import *
import calendar
from datetime import datetime
from time import mktime

def get_id_by_make_name(name):
    data = open_file(const.MODELS_ID_MAPPING_JSON_ROUTE)
    for item in data:
        for sub_item in item['children']:
            if name in sub_item.values():
                key = [key for key, value in sub_item.items() if value == name][0]
                return int(key)
    #print "1"
    
def get_id_by_region_name(name):
    data = open_file(const.COUNTRY_ID_MAPPING_JSON_ROUTE)
    result = []
    for item in data:
        result = list(filter(lambda region_item: region_item['name'] == name, item['regions']))
        if len(result) > 0:
            return result[0]['id']
        
def get_id_by_city_name(name):
    data = open_file(const.COUNTRY_ID_MAPPING_JSON_ROUTE)
    result = []
    for country_item in data:
        for region_item in country_item['regions']:
            result = list(filter(lambda city_item: city_item['name'] == name, region_item['cities']))
            if len(result) > 0:
                return result[0]['id']
            
def get_id_by_name_simple(route, name):
    data = open_file(route)
    result = list(filter(lambda item: item['name'] == name, data))
    return result[0]['id'] if len(result) > 0 else 0

def get_season_by_utcdate(utcdate):
    date_time = datetime.strptime(datetime.fromtimestamp(int(utcdate)).strftime(const.TIME_FORMAT),const.TIME_FORMAT)
    month_number = date_time.month
    season = [key for key, value in const.SEASONS_ENUM.items() if month_number in value][0]
    return season
 
def get_name_by_id_simple(route, id):
    data = open_file(route)
    result = list(filter(lambda item: item['id'] == id, data))
    return result[0]['name']
            
def get_percentiles_for_numeric_column(dataframe, column_name):
    result = QuartileHolder.get_instance().get_quartiles_for_column(column_name)
    if len(result) == 0:
        result = { 'name' : column_name, 'values' : [dataframe.describe()[column_name]['min'], 
                                                            dataframe.describe()[column_name]['25%'], 
                                                            dataframe.describe()[column_name]['50%'], 
                                                            dataframe.describe()[column_name]['75%'], 
                                                            dataframe.describe()[column_name]['max']]}
        QuartileHolder.get_instance().set_quartiles_for_column(result)
    return result
def drop_unhandled_columns(dataframe):
    for column in const.COLUMNS_TO_DROP:
        dataframe = dataframe.drop(column, axis=1)
    return dataframe
 
def process_delta_columns(dataframe):
    #Create delta columns for fields "from" and "to"
#     dataframe['search_volume'] = dataframe['search_volume_to'].astype(int) - dataframe['search_volume_from'].astype(int)
#     dataframe['search_milleage'] = dataframe['search_milleage_to'].astype(int) - dataframe['search_milleage_from'].astype(int)
#     dataframe['search_price'] = dataframe['search_price_to'].astype(int) - dataframe['search_price_from'].astype(int)
#     dataframe['search_year'] = dataframe['search_year_to'].astype(int) - dataframe['search_year_from'].astype(int)
    dataframe['search_volume'] = (dataframe['search_volume_to'] + dataframe['search_volume_from'])/2
    dataframe['search_milleage'] = (dataframe['search_milleage_to'] + dataframe['search_milleage_from'])/2
    dataframe['search_price'] = (dataframe['search_price_to'] + dataframe['search_price_from'])/2
    dataframe['search_year'] = (dataframe['search_year_to'] + dataframe['search_year_from'])/2
    return dataframe

def process_data_ids(dataframe):
    #get ids for corresponding values
    dataframe['search_model'] = dataframe.apply(lambda row: get_id_by_make_name(row['search_model']),axis=1)
    dataframe['search_rigion'] = dataframe.apply(lambda row: get_id_by_region_name(row['search_rigion']),axis=1)
    dataframe['search_city'] = dataframe.apply(lambda row: get_id_by_city_name(row['search_city']),axis=1)
    dataframe['search_country'] = dataframe.apply(lambda row: get_id_by_name_simple(const.COUNTRY_ID_MAPPING_JSON_ROUTE, row['search_country']),axis=1)
    dataframe['search_marka'] = dataframe.apply(lambda row: get_id_by_name_simple(const.MODELS_ID_MAPPING_JSON_ROUTE, row['search_marka']),axis=1)
    dataframe['search_wheel'] = dataframe.apply(lambda row: get_id_by_name_simple(const.WHEELS_ID_MAPPING_JSON_ROUTE, row['search_wheel']),axis=1)
    dataframe['search_body'] = dataframe.apply(lambda row: get_id_by_name_simple(const.BODIES_ID_MAPPING_JSON_ROUTE, row['search_body']),axis=1)
    dataframe['search_transmission'] = dataframe.apply(lambda row: get_id_by_name_simple(const.TRANSMISSIONS_ID_MAPPING_JSON_ROUTE, row['search_transmission']),axis=1)
    return dataframe
def process_numeric_columns(dataframe):
    for column in const.NUMERIC_COLUMNS_REQUIRE_ANALYSIS:
            quartiles = get_percentiles_for_numeric_column(dataframe,column)
            dataframe.loc[ dataframe[column] <= quartiles['values'][1], column] = 0
            dataframe.loc[(dataframe[column] > quartiles['values'][1]) & (dataframe[column] <= quartiles['values'][2]), column] = 1
            dataframe.loc[(dataframe[column] > quartiles['values'][2]) & (dataframe[column] <= quartiles['values'][3]), column]   = 2
            dataframe.loc[ dataframe[column] > quartiles['values'][3], column] = 3
            dataframe[column] = dataframe[column].astype(int)
    return dataframe

def process_date_columns(dataframe):
    for column_name in const.DATE_COLUMNS:
        dataframe[column_name] = dataframe.apply(lambda row: get_season_by_utcdate(row[column_name]),axis=1)
    return dataframe