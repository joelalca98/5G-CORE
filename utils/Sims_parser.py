import logging
import requests
from requests import auth
from requests.auth import HTTPBasicAuth
import json
import sys


with open ("Druid.json", 'r') as f:
    Druid_json = json.load(f)

        #Parse Subnet
try:    
        sims_info = Druid_json['sims_info']
        ki = sims_info['ki']
        opc = sims_info['opc']
        
except:
        print("One of the main parameters in not defined in config file")
        sys.exit(-1)