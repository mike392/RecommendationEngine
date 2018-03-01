'''
Created on Jul 19, 2017

@author: Mikhail_Barsukou
'''
from util.PandasUtils import PandasUtils
from driver.MongoDriver import MongoDriver
import util.Constants as const
import service.DataPreparationHandler
class DatasetHolder(object):
    '''
    classdocs
    '''
    __dataframe = None
    __instance = None

    def __init__(self):
        '''
        Constructor
        '''
        db_instance = MongoDriver.get_instance().get_db_instance(const.DB_INSTANCE)
        data = service.DataPreparationHandler.get_data(db_instance, 'normalized_data')
        self.__dataframe = PandasUtils.get_dataframe(data, const.JSON_STRUCTURE)
        
    @staticmethod
    def get_instance():
        if not DatasetHolder.__instance:
            DatasetHolder.__instance = DatasetHolder()
        return DatasetHolder.__instance
    
    def get_dataset(self):
        return self.__dataframe.copy(deep=True)