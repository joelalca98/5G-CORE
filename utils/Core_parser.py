import requests
from requests import auth
from requests.auth import HTTPBasicAuth
import json
import sys
import logging
from utils import Constant
from utils.Subnet_parser import Druid_json

cons = Constant

with open ("utils/data/Druid.json", 'r') as f: #Utilizar args para indicar el directorio donde está
    Druid_json = json.load(f)

try:
    #Parse druid_info
    druid_info = Druid_json['druid_info']
    username = druid_info['username']
    password = druid_info['password']
    base_ip = druid_info['base_ip']
except:
    logging.info('One of the main parameters of druid_info are not defined in config file')
    sys.exit(-1)

try:
    #Parse core_info
    core_info = Druid_json['core_info']
    amf_iface = core_info['amf_iface']
except:
    print('The parameter amf is not defined in config file')
    sys.exit(-1)

try:
    amf_port = core_info['amf_port']    #Optional
except:
    amf_port = cons.amf_port

try:
    mme_iface = core_info['mme_iface']
except:
    logging.info('The parameter mme is not defined in config file')
    sys.exit(-1)

try:
    mme_port = core_info['mme_port']    #Optional
except:
    mme_port = cons.mme_port

try:
    mgw_iface = core_info['mgw_iface']
except:
    logging.info('The parameter mgw in not defined in config file')
    sys.exit(-1)

    #Parse plmn_info
try:
    plmn_info = Druid_json['plmn_info']
    mcc = plmn_info ['mcc']
    mnc = plmn_info ['mnc']
    network_name = plmn_info ['network_name']
except:
    logging.info('One of the main parameters of plmn are not defined in config file')
    sys.exit(-1)
  