import pandas as pd
import json
import sys
#file path:wget http://labfile.oss.aliyuncs.com/courses/764/user_study.json
def analysis(file,user_id):
    times=0
    minutes=0
    df=pd.read_json(file,orient='records',typ='frame')
    times=df[df['user_id']==int(user_id)]['minutes'].shape[0]
    minutes=df[df['user_id']==int(user_id)]['minutes'].sum()
    return times, minutes


if __name__=='__main__':
    args = sys.argv[1:]
    file_path=args[0]
    user_id=args[1]
    total_times,total_minutes=analysis(file_path,user_id)
    print('for user:',user_id,'total_times are,',total_times,',total minutes are,',total_minutes)
