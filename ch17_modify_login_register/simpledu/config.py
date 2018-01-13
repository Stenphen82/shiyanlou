class BaseConfig(object):
    #config base class#   
    SECRET_KEY = 'very secret key'

class DevelopmentConfig(BaseConfig):
    #development environment config#
    DEBUG = True
    SQLALCHEMY_DATABASE_URI='mysql+mysqldb://root@localhost:3306/simpledu?charset=utf8'
    
class ProductionConfig(BaseConfig):
    #production environment config#
    pass

class TestingConfig(BaseConfig):
    pass

configs = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'testing': TestingConfig
        }



