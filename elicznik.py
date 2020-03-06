#!/usr/bin/env python

import requests
from requests import adapters
import ssl
from urllib3 import poolmanager
import datetime

#Add login details & meter ID here:
username = 'TAURON_USERNAME'
password = 'TAURON_PASSWORD'
meter_id = TAURON_ENERGY_METER_ID

payload = { 
                'username': username,
                'password': password ,
                'service': 'https://elicznik.tauron-dystrybucja.pl'
}

url = 'https://logowanie.tauron-dystrybucja.pl/login'
charturl = 'https://elicznik.tauron-dystrybucja.pl/index/charts'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'} 

class TLSAdapter(adapters.HTTPAdapter):

    def init_poolmanager(self, connections, maxsize, block=False):
        """Create and initialize the urllib3 PoolManager."""
        ctx = ssl.create_default_context()
        ctx.set_ciphers('DEFAULT@SECLEVEL=1')
        self.poolmanager = poolmanager.PoolManager(
                num_pools=connections,
                maxsize=maxsize,
                block=block,
                ssl_version=ssl.PROTOCOL_TLS,
                ssl_context=ctx)

session = requests.session()
session.mount('https://', TLSAdapter())

p = session.request("POST", url, data=payload, headers=headers)
p = session.request("POST", url, data=payload, headers=headers)

chart = {
	        #change timedelta to get data from another days (1 for yesterday)
                "dane[chartDay]": (datetime.datetime.now() - datetime.timedelta(1)).strftime('%d.%m.%Y'),
                "dane[paramType]": "day",
                "dane[smartNr]": meter_id,
	        #comment if don't want generated energy data in JSON output:
                "dane[checkOZE]": "on"
}

r = session.request("POST", charturl, data=chart, headers=headers)
print(r.text)

#Optionally write JSON to file
#with open('file.json', 'wb') as f:
#    f.write(r.content)
