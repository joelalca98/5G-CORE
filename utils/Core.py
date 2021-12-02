import requests
from requests import auth
from requests.auth import HTTPBasicAuth
from utils import Core_parser
from utils import Subnet_parser
from utils import Session
from utils.Request import Request


# parserCore = Core  #Creando instancia de la clase Core
# core = Core.Core(parserCore.Core_parser)
# core.call_core(parserCore.Core_parser) #Aplicar if  --> 0 ok
request = Request

class Core:
    def __init__(self, parser):
        self.amf_iface = parser.amf_iface
        self.amf_port = parser.amf_port
        self.mme_iface = parser.mme_iface
        self.mme_port = parser.mme_port
        self.mgw_iface = parser.mgw_iface
        self.mcc = parser.mcc
        self.mnc = parser.mnc
        self.network_name = parser.network_name
        
    def call_core (self, parser): #Aplicar try
        IP_AMF = 'https://' + parser.base_ip + ':443' '/api' '/amf?id=1'
        argsAmf = { 
        'n2_net_device' : parser.amf_iface,
        'n2_port': parser.amf_port
               }
        typeAmf = 'Amf'
        #En otra clase
        # request.putCall(request,IP_AMF,argsAmf,typeAmf)

        #Modify MME
        BASE_IP_MME = 'https://' + parser.base_ip + ':443' '/api' '/mme?id=1'
        argsMme = { 
        's1mme_net_device' : parser.mme_iface,
        's1mme_port': parser.mme_port
               }
        # request.putCall(request,BASE_IP_MME,argsMme)
        typeMme = 'Mme'

        #Modify mgw https://192.168.40.124/api/mgw_endpoint?id=1
        BASE_IP_MGW = 'https://' + parser.base_ip + ':443' '/api' '/mgw_endpoint?id=1'
        argsMgw = { 
           'net_device': parser.mgw_iface
        }
        typeMgw = 'Mgw'
        # request.putCall(request, BASE_IP_MGW, argsMgw)

        #Modify PLMN 'https://192.168.40.124:443/api/plmn?id=1'
        BASE_IP_PLMN = 'https://' + parser.base_ip + ':443' '/api' '/plmn?id=1'
        argsPlmn = { 
           'mcc': parser.mcc,
           'mnc': parser.mcc,
           'short_network_name': parser.network_name,
           'full_network_name': parser.network_name
        }
        typePlmn = 'Plmn'
        # request.putCall(request,BASE_IP_PLMN,argsPlmn)
        try:
            request.putCall(request,IP_AMF,argsAmf,typeAmf)
            request.putCall(request,BASE_IP_MME,argsMme,typeMme)
            request.putCall(request, BASE_IP_MGW, argsMgw, typeMgw)
            request.putCall(request,BASE_IP_PLMN,argsPlmn, typePlmn)
            return 0
        except:
            return -1


