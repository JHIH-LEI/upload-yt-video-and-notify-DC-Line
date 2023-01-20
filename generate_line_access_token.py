# issue channel access token v2.1
import dotenv
import requests
from os import getenv
from dotenv import (find_dotenv, set_key, load_dotenv)
from json import loads

load_dotenv()
print(getenv('JWT'))
url = 'https://api.line.me/oauth2/v2.1/token'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
data = {'grant_type': 'client_credentials',
        'client_assertion_type': 'urn:ietf:params:oauth:client-assertion-type:jwt-bearer',
        f'client_assertion': {getenv('JWT')}}

response = requests.post(url, headers=headers, data=data)
dotenv_file = find_dotenv()
print(loads(response.text))
set_key(dotenv_file, 'LINE_CHANNEL_ACCESS_TOKEN', loads(response.text)['access_token'])

print('channel access token v2.1:\n')
print(f'{response.text}\n')
print('Store access_token and kid_id\n')
