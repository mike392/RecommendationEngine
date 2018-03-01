'''
Created on Jul 14, 2017

@author: Mikhail_Barsukou
'''

class IdGenerator(object):
    '''
    classdocs
    '''
    __instance = None
    __id = 0

    def __init__(self):
        '''
        Constructor
        '''
        
    @staticmethod
    def get_instance():
        if not IdGenerator.__instance:
            IdGenerator.__instance = IdGenerator()
        return IdGenerator.__instance
    
    def get_id(self):
        self.__id += 1
        return self.__id