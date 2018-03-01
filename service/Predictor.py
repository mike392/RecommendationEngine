'''
Created on Jul 19, 2017

@author: Mikhail_Barsukou
'''
import xgboost as xgb
from service.DataPreparationHandler import *
import pandas as pd
from util.DataPreparationUtils import get_name_by_id_simple
from datetime import datetime
from sklearn.metrics import accuracy_score

class Predictor(object):
    '''
    classdocs
    '''
    __instance = None
    __model = None

    def __init__(self):
        '''
        Constructor
        '''
        self.__model = xgb.XGBClassifier()
        #print "predictor constructor called"
    
    @staticmethod
    def get_instance():
        if not Predictor.__instance:
            Predictor.__instance = Predictor()
        return Predictor.__instance
    
    def train_model(self):
        d1 = datetime.now()
        train_features, test_features, train_labels, test_labels = get_prepared_data_for_target(const.TARGET_COLUMN)
        print ('Training started....')
        self.__model.fit(train_features, train_labels)
        predicted_labels = self.__model.predict(test_features)
        predictions = [round(value) for value in predicted_labels]
        d2 = datetime.now()
        delta = d2 - d1
        return { 'Training time' : str(delta.seconds) + ' seconds',
                'Model accuracy' : accuracy_score(test_labels, predictions) }
    
    def predict_value(self, parameters):
        d1 = datetime.now()
        features = pd.DataFrame(data=parameters,columns=const.JSON_STRUCTURE, index=[0])
        features = process_data(features)
        features = features.drop(const.TARGET_COLUMN, axis=1)
        value = self.__model.predict(features)
        d2 = datetime.now()
        delta = d2 - d1
        return { 'Predicted car model' : get_name_by_id_simple(const.MODELS_ID_MAPPING_JSON_ROUTE, value),
                'Prediction time' : str(delta.microseconds / 1000) + ' milliseconds'}