import pandas as pd
import json
import sys
import matplotlib.pyplot as plt
from pandas import Series, DataFrame
import numpy as np

#file path:wget http://labfile.oss.aliyuncs.com/courses/764/user_study.json

df=pd.read_json('/home/shiyanlou/Code/user_study.json',orient='records',typ='frame'    )


def figure():
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    data=df.groupby('user_id').sum().head(1000)
    ax.plot(data.index, data.minutes)
    ax.set_title("StudyData")
    ax.set_xlabel("User ID")
    ax.set_ylabel("Study Time")
    plt.show()

if __name__=='__main__':
    figure()
                                                    #print('for user:',user_id,'total_times are,',total_times,',total minutes are,',total_minutes)
