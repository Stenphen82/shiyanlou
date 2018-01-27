import os
import json
from flask import Flask

def create_app():
    app = Flask('rmon')
    file = os.envrion.get('RMON_CONFIG')
    data1 = ''
    with open(file,'r') as read_file:
        for x in read_file:
            if '#' in x:
                continue
            else:
                data1=data1+x.strip()

    config_dict=json.loads(data1)
    
    for key,value in config_dict.items():
        app.config[key.upper()]=value
    
    return app
