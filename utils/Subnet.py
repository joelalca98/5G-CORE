import requests
from requests import auth
from requests.auth import HTTPBasicAuth
from utils import Core_parser
from utils import Subnet_parser
from utils import Request
import requests
from requests import auth
from requests.auth import HTTPBasicAuth
from utils import Core_parser
from utils import Subnet_parser
from utils import Session
from utils.Request import Request


request = Request

class Subnet:
    def __init__(self, parser):
        self.apn = parser.apn
        self.tun_addr_ip = parser.tun_addr_ip
        self.tun_netmask = parser.tun_netmask
        self.ipv4_pool_first_ip = parser.ipv4_pool_first_ip
        self.ipv4_pool_last_ip = parser.ipv4_pool_last_ip
        #QoS
        self.qci = parser.qci
        self.dl_apn_ambr = parser.dl_apn_ambr
        self.ul_apn_ambr = parser.ul_apn_ambr
        self.priority = parser.priority
        self.may_trigger_preemption = parser.may_trigger_preemption
        self.preemptable = parser.preemptable
        
    def call_subnet (self, parser):
       
       #Create ipv4_pool  OK
        IP_SPP = 'https://' + parser.base_ip + ':443' '/api' '/ipv4_pool'
        args = { 
                   "id": 3,
                   "name": parser.apn,
                   "first_ip" : parser.ipv4_pool_first_ip,
                   "last_ip" : parser.ipv4_pool_last_ip
               }
        request.postCall(request, IP_SPP, args)
       
        #Create subnet    OK
        IP_CreateSubnet = 'https://' + parser.base_ip + ':443' '/api' '/pdn'
        args = { 
                   "id": 6,
                   "apn": parser.apn,
                   "primary_dns": "8.8.8.8",
                   "secondary_dns": "8.8.4.4",
                   "ipv4_pool_id": 3,
                   "ep_group_id": 2,
                   "allow_multiple_connections": 0
               }
        request.postCall(request, IP_CreateSubnet, args)

        #Activate subnet create previously   OK
        IP_ActivateSubnet = 'https://' + parser.base_ip + ':443' '/api' '/subscription_profile'
        args = { 
                   "id": 6,
                   "apn": parser.apn,
                   "qci": parser.qci,
                   "priority": parser.priority,
                   "may_trigger_preemption": parser.may_trigger_preemption,
                   "preemptable": parser.preemptable,
                   "allow_multiple_connections": 0
               }
        request.postCall(request, IP_ActivateSubnet, args)

        #Delete other networks
        #Delete Network 1     OK
        IP_DeleteSubnets1 = 'https://' + parser.base_ip + ':443' '/api' '/pdn?id=1'  
        args = { 
               }
        response = requests.delete(IP_DeleteSubnets1, auth=HTTPBasicAuth(username=parser.username,password=parser.password),verify=False, json=args)
        response_info = response.json()
        print(response_info)
        #Delete Network 2   NO OK --> AL SEGUNDO INTENTO SI
        IP_DeleteSubnets2 = 'https://' + parser.base_ip + ':443' '/api' '/pdn?id=2'
        args = { 
               }
        response = requests.delete(IP_DeleteSubnets2, auth=HTTPBasicAuth(username=parser.username,password=parser.password),verify=False, json=args)
        response_info = response.json()
        print(response_info)
        #Delete Network 3   NO OK --> AL TERCER INTENTO SI
        IP_DeleteSubnets3 = 'https://' + parser.base_ip + ':443' '/api' '/pdn?id=3'
        args = { 
               }
        response = requests.delete(IP_DeleteSubnets3, auth=HTTPBasicAuth(username=parser.username,password=parser.password),verify=False, json=args)
        response_info = response.json()
        print(response_info)
        #Create Subscription_Profile_Preference   OK
        IP_SPP = 'https://' + parser.base_ip + ':443' '/api' '/subscription_profile_preference'
        args = { 
                   "id": 1,
                   "name": parser.apn,
                   "subscription_profile_1_id": 6,
                   "subscription_profile_2_id": 0,
                   "subscription_profile_3_id": 0,
                   "subscription_profile_4_id": 0,
                   "subscription_profile_5_id": 0
               }
        request.postCall(request,IP_SPP, args)
        #Create Group   OK
        IP_Group = 'https://' + parser.base_ip + ':443' '/api' '/group'
        args = { 
                   "id": 1,
                   "num": "1",
                   "name": parser.apn,
                   "imsi_prefix": "",
                   "description": parser.apn,
                   "subscription_profile_preference_id":1
               }
        response = requests.post(IP_Group, auth=HTTPBasicAuth(username=parser.username,password=parser.password),verify=False, json=args)
        response_info = response.json()
        print(response_info)
        #FALTA UNIR GRUPO CON USERS (USERS AUN NO CREADOS) Y EL IPROUTE CON SU NETMASK