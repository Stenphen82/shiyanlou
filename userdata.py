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
        return float(self._config['YangLao'])+float(self._config['YiLiao'])+float(self._config['ShiYe'])+float(self._config['GongShang'])+float(self._config['ShengYu'])+float(self._config['GongJiJin'])

config1=Config('/home/shiyanlou/test.cfg')
#config1.get_config()

class UserData(object):
    def __init__(self,userdatafile):
        self._userdata={}
        self._userdatafile=userdatafile

        with open(self._userdatafile) as file:
            for x in file:
                key,value=x.split(',')
                self._userdata[key]=value

    def Salary(self):
        for key,value in self._userdata.items():

            Insurance = int(value) * config1.get_basenumber()
            TaxIncome = int(value) - Insurance - 3500
    
            if TaxIncome < 0:
                Tax= 0
            elif TaxIncome <= 1500:
                Tax=TaxIncome * 0.03
            elif TaxIncome > 1500 and TaxIncome <=4500:
                Tax=TaxIncome * 0.1 - 105
            elif TaxIncome > 4500 and TaxIncome <=9000:
                Tax=TaxIncome * 0.2 - 555
            elif TaxIncome > 9000 and TaxIncome <=35000:
                Tax=TaxIncome * 0.25 - 1005
            elif TaxIncome > 35000 and TaxIncome <=55000:
                Tax=TaxIncome * 0.3 - 2755
            elif TaxIncome > 55000 and TaxIncome <=80000:
                Tax=TaxIncome * 0.35 - 5505
            else:
                Tax=TaxIncome * 0.45 - 13505

            Post_Salary = int(value) - Insurance - Tax
            print(key,value,Post_Salary)
#            return format(Post_Salary,'.2f')

    def get_userdata(self):
        for key,value in self._userdata.items():
            print(key,value)

user1=UserData('/home/shiyanlou/user1.csv')
user1.get_userdata()
user1.Salary()
