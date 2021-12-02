# #  !/usr/bin/python3
# import sys
# from datetime import datetime
# from threading import Thread, Lock, currentThread
# import json
# from datetime import datetime, timedelta
# from requests import Request, Session, exceptions, codes
# from requests.adapters import HTTPAdapter
# from urllib3.util import Retry
# from requests import HTTPAdapter
# from colors import bcolors


# class Session:
#    def custom_session(self, retries=2, backoff_factor=0.1, status_forcelist=(500, 503, 504, 400, 404)):
#         '''Creates an HTTP Session with defined number of retries and backoff factor'''
#         session = Session()
#         retry = Retry(
#             total=retries,
#             read=retries,
#             connect=retries,
#             backoff_factor=backoff_factor,
#             status_forcelist=status_forcelist,
#         )
#         adapter = HTTPAdapter(max_retries=retry)
#         session.mount('http://', adapter)
#         session.mount('https://', adapter)
#         return session


#    def try_request(self, session, method, url, params=None):
#         '''Auxiliar method to handle Exceptions during requests'''

#         try:
#             if method == 'GET':
#                 response = self.session.get(
#                     url, params=params, timeout=self.config['TIMEOUT'])
#             elif method == 'POST':
#                 response = self.session.post(
#                     url, params=params, timeout=self.config['TIMEOUT'])
#             elif method == 'PUT':
#                 response = self.session.put(
#                     url, params=params, timeout=self.config['TIMEOUT'])
#             response.raise_for_status()

#         except exceptions.HTTPError as error:
#             error_msg = '{}>>> **ERROR in action {}. Type {}** Args: {}{}'.format(
#                 bcolors.FAIL, action, type(error).__name__, error.args, bcolors.ENDC)

#         except exceptions.RetryError as error:
#             error_msg = '{}>>> **ERROR in action {}. Type {}** Args: {}{}'.format(
#                 bcolors.FAIL, action, type(error).__name__, error.args, bcolors.ENDC)

#         except exceptions.ConnectionError as error:
#             error_msg = '{}>>> **ERROR in action {}. Type {}** Args: {}{}'.format(
#                 bcolors.FAIL, action, type(error).__name__, error.args, bcolors.ENDC)
#         finally:
#             if error_msg is not None:
#                 print(error_msg)

#             return response