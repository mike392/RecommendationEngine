'''
Created on Jul 19, 2017

@author: Mikhail_Barsukou
'''
import sys
import web
from util.IdGenerator import IdGenerator
from service.DataStub import generate_data_record
from service.Predictor import Predictor


urls = (
        '/id', 'get_id',
        '/data', 'get_data',
        '/train', 'train_model',
        '/predict', 'predict_value'
    )

app = web.application(urls, globals())
web.config.debug = True
options = {"host" : sys.argv[1],
           "port" : sys.argv[2]}
class get_id:
    def GET(self):
        return IdGenerator.get_instance().get_id()
    
class get_data:
    def GET(self):
        return generate_data_record()
    
class train_model:
    def GET(self):
        return Predictor.get_instance().train_model()
    
class predict_value:
    def GET(self):
        params = web.input()
        return Predictor.get_instance().predict_value(dict(params))
    
if __name__ == '__main__':
    web.httpserver.runsimple(app.wsgifunc(), (options["host"], int(options["port"])))