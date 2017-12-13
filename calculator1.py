#!/usr/bin/env python3
def Salary(Number):

    Insurance = Number * 0.165
    TaxIncome = Number - Insurance - 3500
    
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

    Post_Salary = Number - Insurance - Tax
    return format(Post_Salary,'.2f')


import sys
dict={}        
try:
    for arg in sys.argv[1:]:
        key,value=arg.split(':')
    
        if int(value) < 0:
            raise ValueError()
        else:
            dict[int(key)]=Salary(int(value))
    
    for key,value in dict.items():
        print(str(key)+':'+str(value))       

except IndexError:
    print("Parameter Error")
except ValueError:
    print("Parameter Error")

