import requests
from requests.auth import HTTPBasicAuth
from utils import Core_parser
from utils import Subnet_parser
from utils import Core
from utils import Subnet
from utils import Request

request = Request
#CORE
parserCore = Core  #Creando instancia de la clase Core
core = Core.Core(parserCore.Core_parser)
core.call_core(parserCore.Core_parser) #Aplicar if  --> 0 ok


#SUBNET
# parserSubnet = Subnet
# subnet = Subnet.Subnet(parserSubnet.Subnet_parser)
# subnet.call_subnet(parserSubnet.Subnet_parser) #No va porq hay cosas que aun no están creadas xd

# if core.call_core(parserCore.Core_parser) == 0:

