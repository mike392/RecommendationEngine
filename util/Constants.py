# -*- coding: utf-8 -*-
'''
Created on Jul 14, 2017

@author: Mikhail_Barsukou
'''
PORT = 27017
#HOST = "185.66.69.113"
HOST = "127.0.0.1"
DATA_STRUCTURE = ("id", "value", "timestamp")
DB_INSTANCE = "BigDataABW"
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
MODELS_JSON_ROUTE = '../resource/Model.json'
MODELS_ID_MAPPING_JSON_ROUTE = '../resource/ModelIdMapping.json'
COUNTRY_ID_MAPPING_JSON_ROUTE = '../resource/CountryIdMapping.json'
TRNASMISSIONS_JSON_ROUTE = '../resource/Transmission.json'
TRANSMISSIONS_ID_MAPPING_JSON_ROUTE = '../resource/TransmissionIdMapping.json'
COUNTRIES_JSON_ROUTE = '../resource/Country.json'
BODIES_JSON_ROUTE = '../resource/Body.json'
BODIES_ID_MAPPING_JSON_ROUTE = '../resource/BodyIdMapping.json'
WHEELS_JSON_ROUTE = '../resource/Wheel.json'
WHEELS_ID_MAPPING_JSON_ROUTE = '../resource/WheelIdMapping.json'

ENGINE_VOLUME_UPPER_BOUND = 8000
MILLEAGE_UPPER_BOUND = 1000000
YEAR_LOWER_BOUND = 1960
PRICE_UPPER_BOUND = 400000
ROWS_NUMBER_LIMIT = 50000
SEASONS_ENUM = {1:[12,1,2],
                2:[3,4,5],
                3:[6,7,8],
                4:[9,10,11]}
DATE_COLUMNS = ["last_login"]
NUMERIC_COLUMNS_REQUIRE_ANALYSIS = [
    "search_volume",
    "search_milleage",
    "search_year",
    "search_price"
    ]

COLUMNS_TO_DROP = [
    "search_engine",
    "search_text",
    "search_condition",
    "search_milleage_from",
    "search_milleage_to",
    "search_volume_from",
    "search_volume_to",
    "search_price_from",
    "search_price_to",
    "search_year_from",
    "search_year_to"
    ]
TARGET_COLUMN = "search_marka"
JSON_STRUCTURE = (
"last_login",
"search_body",
"search_city",
"search_condition",
"search_country",
"search_engine",
"search_marka",
"search_milleage_from",
"search_milleage_to",
"search_model",
"search_price_from",
"search_price_to",
"search_rigion",
"search_text",
"search_transmission",
"search_volume_from",
"search_volume_to",
"search_wheel",
"search_year_from",
"search_year_to",
"user_id")


