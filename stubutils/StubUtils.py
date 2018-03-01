'''
Created on Jul 17, 2017

@author: Mikhail_Barsukou
'''
import util.Constants as const
import json
import os
import random 
import datetime
from time import mktime
from io import open
from datetime import timedelta


def get_random_model():
    data = open_file(const.MODELS_JSON_ROUTE)
    models = [item["name"] for item in data["tree"]]
    return random.choice(models)

def get_random_make(model):
    data = open_file(const.MODELS_JSON_ROUTE)
    makes = [item["children"] for item in data["tree"] if item["name"] == model]
    return random.choice(makes[0])

def get_random_date():
    start = datetime.datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
    end = datetime.datetime.now()
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    result = datetime.datetime.utctimetuple(start + timedelta(seconds=random_second))
    return mktime(result)

def get_random_volume_from():
    return random.choice(range(0,const.ENGINE_VOLUME_UPPER_BOUND))

def get_random_volume_to(volume):
    return random.choice(range(volume, const.ENGINE_VOLUME_UPPER_BOUND))

def get_random_transmission():
    data = open_file(const.TRNASMISSIONS_JSON_ROUTE)
    transmissions = data["possible_values"]
    return random.choice(transmissions)

def get_random_milleage_from():
    return random.choice(range(0,const.MILLEAGE_UPPER_BOUND))

def get_random_milleage_to(milleage):
    return random.choice(range(milleage, const.MILLEAGE_UPPER_BOUND))

def get_random_country():
    data = open_file(const.COUNTRIES_JSON_ROUTE)
    countries = [item["name"] for item in data["tree"].values()]
    return random.choice(countries)

def get_random_region(country):
    data = open_file(const.COUNTRIES_JSON_ROUTE)
    region_dicts = [item["children"] for item in data["tree"].values() if item["name"] == country]
    regions = [item["region"] for item in region_dicts[0].values()]
    return random.choice(regions)

def get_random_city(country, region):
    data = open_file(const.COUNTRIES_JSON_ROUTE)
    region_dicts = [item["children"] for item in data["tree"].values() if item["name"] == country]
    try:
        city_dict = [item["city"] for item in region_dicts[0].values() if item["region"] == region]
    except KeyError:
        #print region
        raise
    cities = list(city_dict[0].values())
    return random.choice(cities)

def get_random_body():
    data = open_file(const.BODIES_JSON_ROUTE)
    bodies = data["possible_values"]
    return random.choice(bodies)

def get_random_wheel():
    data = open_file(const.WHEELS_JSON_ROUTE)
    wheels = data["possible_values"]
    return random.choice(wheels)

def get_random_year_from():
    current_year = datetime.date.today().year
    return random.choice(range(const.YEAR_LOWER_BOUND, current_year))

def get_random_year_to(year):
    current_year = datetime.date.today().year
    return random.choice(range(year, current_year))

def get_random_price_from():
    return random.choice(range(0, const.PRICE_UPPER_BOUND))

def get_random_price_to(price):
    return random.choice(range(price, const.PRICE_UPPER_BOUND))
    
def open_file(route):
    json_file = open(os.path.join(os.path.dirname(__file__),route), encoding='utf8').read()
    data = json.loads(json_file, encoding = 'utf8')
    return data