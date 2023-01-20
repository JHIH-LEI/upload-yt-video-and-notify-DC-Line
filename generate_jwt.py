import jwt
from jwt.algorithms import RSAAlgorithm
import time

from dotenv import (load_dotenv, set_key, find_dotenv)
from os import getenv
import json

with open('private_key.json', 'r') as json_file:
    private_key = json.load(json_file)

load_dotenv()

channel_id = getenv('LINE_CHANNEL_ID')

headers = {
    'alg': 'RS256',
    'typ': 'JWT',
    'kid': getenv('KID')
}

payload = {
    'iss': channel_id,
    'sub': channel_id,
    'aud': 'https://api.line.me/',
    'exp': int(time.time()) + (60 * 30),
    'token_exp': 60 * 60 * 24 * 30
}

key = RSAAlgorithm.from_jwk(private_key)

JWT = jwt.encode(payload, key, algorithm='RS256', headers=headers, json_encoder=None)

dotenv_file = find_dotenv()
set_key(dotenv_file, 'JWT', JWT)

print('JWT: \n')
print(f'{JWT}\n')
