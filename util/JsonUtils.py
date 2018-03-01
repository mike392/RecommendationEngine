'''
Created on Jul 18, 2017

@author: Mikhail_Barsukou
'''
from stubutils.StubUtils import *

def models_json_update():
        data = open_file(const.MODELS_JSON_ROUTE)
        result_list = []
        for idx, item in enumerate(data['tree']):
            result = {}
            result['id'] = idx+1
            result['name'] = item['name']
            result['children'] = []
            for idx, inner_item in enumerate(item['children']):
                result['children'].append({ idx+1 : inner_item})
                #print inner_item
            result_list.append(result)
        with open(os.path.join(os.path.dirname(__file__), const.MODELS_ID_MAPPING_JSON_ROUTE), 'w') as fp:
            json.dump(result_list, fp)
            
def country_json_update():
        data = open_file(const.COUNTRIES_JSON_ROUTE)
        result_list = []
        for country_ind, country_item in enumerate(data['tree'].values()):
            country_result = {}
            country_result['id'] = country_ind+1
            country_result['name'] = country_item['name']
            country_result['regions'] = []
            for region_ind, region_item in enumerate(country_item['children'].values()):
                region_result = {}
                region_result['id'] = region_ind+1
                region_result['name'] = region_item['region']
                region_result['cities'] = []
                for city_ind, city_item in enumerate(region_item['city'].values()):
                    city_result = {}
                    city_result['id'] = city_ind+1
                    city_result['name'] = city_item
                    region_result['cities'].append(city_result)
                country_result['regions'].append(region_result)
            result_list.append(country_result)
        with open(os.path.join(os.path.dirname(__file__), const.COUNTRY_ID_MAPPING_JSON_ROUTE), 'w') as fp:
            json.dump(result_list, fp)
            
def body_transmission_wheel_json_update():
    simple_json_update(const.BODIES_JSON_ROUTE, const.BODIES_ID_MAPPING_JSON_ROUTE)
    simple_json_update(const.TRNASMISSIONS_JSON_ROUTE, const.TRANSMISSIONS_ID_MAPPING_JSON_ROUTE)
    simple_json_update(const.WHEELS_JSON_ROUTE, const.WHEELS_ID_MAPPING_JSON_ROUTE)

def simple_json_update(src_route, dest_route):
    data = open_file(src_route)
    result_list = []
    for idx, item in enumerate(data['possible_values']):
        result = {}
        result['id'] = idx+1
        result['name'] = item
        result_list.append(result)
    with open(os.path.join(os.path.dirname(__file__), dest_route), 'w') as fp:
            json.dump(result_list, fp)