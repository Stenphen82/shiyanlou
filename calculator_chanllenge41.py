#!/usr/bin/env python3
from multiprocessing import Process, Queue
import sys
import os.path
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

    def get_JiShuL(self):
        return float(self._config['JiShuL'])

    def get_JiShuH(self):
        return float(self._config['JiShuH'])

    def get_basenumber(self):
        return float(self._config['YangLao'])+float(self._config['YiLiao'])+float(self._config['ShiYe'])+float(self._config['GongShang'])+float(self._config['ShengYu'])+float(self._config['GongJiJin'])


class UserData(object):
    def __init__(self,userdatafile):
        self._userdata={}
        self._userdatafile=userdatafile

    def ReadUserData(self):
        with open(self._userdatafile) as file:
            for x in file:
                x=x.strip('\n')
                key,value=x.split(',')
                self._userdata[key]=value
   
        queue1.put(self._userdata)
        return self._userdata

    def Salary(self):
        output=[]
        dict_original=queue1.get()

        for key,value in dict_original.items():

            if int(value) < config1.get_JiShuL():
                Insurance = config1.get_JiShuL() * config1.get_basenumber()
            elif int(value) > config1.get_JiShuH():
                Insurance = config1.get_JiShuH() * config1.get_basenumber()
            else:
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
            output.append(key+','+value+','+str(format(Insurance,'.2f'))+','+str(format(Tax,'.2f'))+','+str(format(Post_Salary,'.2f')))
        queue2.put(output)
        return output

    def WriteFile(self):
        dict_post=queue2.get()
        with open(outputfile,'a') as file:    
            for i in range(len(dict_post)):
                file.write(dict_post[i]+'\n')

if __name__=='__main__':
    args = sys.argv[1:]
    try:
        indexC=args.index('-c')
        configfile=args[indexC+1]
        if not os.path.exists(configfile):
            raise FileNotFoundError()

        indexD=args.index('-d')
        userfile=args[indexD+1]
        if not os.path.exists(userfile):
            raise FileNotFoundError()

        indexO=args.index('-o')
        outputfile=args[indexO+1]
        
        queue1=Queue()
        queue2=Queue()
        
        config1=Config(configfile)
        userdata1=UserData(userfile)

        p1=Process(target=userdata1.ReadUserData)
        p1.start()
        p1.join()

        p2=Process(target=userdata1.Salary)
        p2.start()
        p2.join()
        
        p3=Process(target=userdata1.WriteFile)
        p3.start()
        p3.join()       


    except FileNotFoundError:
        print('file paths are not correct!')
        

#user1=UserData('/home/shiyanlou/user1.csv')
#user1.get_userdata()
#user1.Salary()

