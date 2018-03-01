'''
Created on Jul 19, 2017

@author: Mikhail_Barsukou
'''

class QuartileHolder(object):
    '''
    classdocs
    '''
    __quartiles = None
    __instance = None

    def __init__(self):
        '''
        Constructor
        '''
        self.__quartiles = []
    @staticmethod
    def get_instance():
        if not QuartileHolder.__instance:
            QuartileHolder.__instance = QuartileHolder()
        return QuartileHolder.__instance
    
    def set_quartiles_for_column(self, quartiles_for_column):
        self.__quartiles.append(quartiles_for_column)
        
    def get_quartiles_for_column(self, name):
        return list(filter(lambda item : item['name'] == name, self.__quartiles))