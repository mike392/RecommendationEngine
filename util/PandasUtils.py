'''
Created on Jul 18, 2017

@author: Mikhail_Barsukou
'''
import pandas

class PandasUtils:
    @staticmethod
    def get_dataframe(dataset, columns_list):
        return pandas.DataFrame(data=dataset,columns=columns_list)
    @staticmethod
    def get_avg_for_column(dataframe, column_name):
        return dataframe[column_name].mean()