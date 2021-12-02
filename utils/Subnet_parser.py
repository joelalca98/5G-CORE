import logging
import requests
from requests import auth
from requests.auth import HTTPBasicAuth
import json
import sys
from utils import Constant

cons = Constant

with open ("utils/data/Druid.json", 'r') as f:
    Druid_json = json.load(f)

        #Parse Subnet
try:    
        druid_info = Druid_json['druid_info']
        username = druid_info['username']
        password = druid_info['password']
        base_ip = druid_info['base_ip']
except:
    logging.info('One of the main parameters of druid_info are not defined in config file')
    sys.exit(-1)

try:
        subnet_info = Druid_json['subnet_info']
        apn = subnet_info['apn']
except:
    print('The parameter apn is not defined in config file')
    sys.exit(-1)

try:
        tun_addr_ip = subnet_info['tun_addr_ip']
except:
    print('The parameter apn is not defined in config file')
    sys.exit(-1)

try:
        tun_netmask = subnet_info['tun_netmask']
except:
    print('The parameter tun_netmask is not defined in config file')
    sys.exit(-1)

try:
        ipv4_pool_first_ip = subnet_info['ipv4_pool_first_ip']
except:
    print('The parameter ipv4_pool_first_ip is not defined in config file')
    sys.exit(-1)

try:
        ipv4_pool_last_ip = subnet_info['ipv4_pool_last_ip']
except:
    print('The parameter ipv4_pool_last_ip is not defined in config file')
    sys.exit(-1)

try:
        #Parse QoS
        qos = subnet_info['qos']
        qci = qos['qci']
        dl_apn_ambr = qos['dl_apn_ambr']
        ul_apn_ambr = qos['ul_apn_ambr']
        priority = qos['priority']
        may_trigger_preemption = qos['may_trigger_preemption']
        preemptable = qos['preemptable']
        
except:
        qci = cons.qci
        dl_apn_ambr = cons.dl_apn_ambr
        ul_apn_ambr = cons.ul_apn_ambr
        priority = cons.priority
        may_trigger_preemption = cons.may_trigger_preemption
        preemptable = cons.preemptable