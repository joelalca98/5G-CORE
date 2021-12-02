import requests
import json
from requests import auth
from requests.auth import HTTPBasicAuth
from utils import Core_parser
from utils import Subnet_parser

http = HTTPBasicAuth(username=Core_parser.username,password=Core_parser.password)

class Request:
    def __init__(self, url, auth, args):
        self.url = url
        self.auth = auth
        self.args = args

    def putCall (self, url, args, type):
        try:
            response = requests.put(url, auth=http, verify=False, json = args)
            if(response.status_code == 200):
                response_info = response.json()
                print(response_info)
                return 0
            if(response.status_code == 401):
                print("Error en la autentificacion")
        except:
            print ("Error PUT" + " " + type)
            return -1

    # def postCall (self, url, args):
    #     try:
    #         response = requests.post(url, auth=http, verify=False, json = args)
    #         response_info = response.json()
    #         print(response_info)
    #         return 0
    #     except:
    #         print ("Error POST")
    #         return -1