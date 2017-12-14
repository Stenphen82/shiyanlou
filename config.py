class Config(object):
    def __init__(self,configfile):
        self._config={}
        self._configfile=configfile
        with open(self._configfile) as file:
            for x in file:
                key,value=x.split('=')
                self._config[key.strip()]=value.strip()

    def get_config(self):        
        for key,value in self._config.items():
            print(key,value)
    
    def get_basenumber(self):
        basenumber=float(self._config['YangLao'])+float(self._config['YiLiao'])+float(self._config['ShiYe'])+float(self._config['GongShang'])+float(self._config['ShengYu'])+float(self._config['GongJiJin'])
        print(basenumber)
config1=Config('/home/shiyanlou/test.cfg')
config1.get_config()
config1.get_basenumber()
