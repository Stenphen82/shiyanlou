#!/usr/bin/env python3
import sys

try:
    Payment=sys.argv[1]
    Payment=int(Payment)
    Insurance = 0
    TaxIncome = Payment - Insurance - 3500
    if Payment < 0:
            raise ValueError()
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

    print(format(Tax,'.2f'))
except IndexError:
    print("Parameter Error")
except ValueError:
    print("Parameter Error")

