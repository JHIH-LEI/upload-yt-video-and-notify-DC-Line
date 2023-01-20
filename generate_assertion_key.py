from jwcrypto import jwk
import json

key = jwk.JWK.generate(kty='RSA', alg='RS256', use='sig', size=2048)

private_key = key.export_private()
public_key = key.export_public()

# store private_key in private_key.json file
# json.load把str -> dict json.dumps把dict -> json
data = json.dumps(json.loads(private_key))

with open('private_key.json', 'w') as json_file:
    json_file.write(data)

print('private key \n' + json.dumps(json.loads(private_key), indent=2))
print('public key \n' + json.dumps(json.loads(public_key), indent=2))
print('Copy entire public key.\n -> Go to "https://developers.line.biz/console/" \n'
      'choose your channel\n -> Register Assertion Signing Key in basic setting page.\n')
print('When you successfully Register Assertion Signing Key You Will See Kid On The Screen.\n')
print('*** Copy Your Kid to .env file as KID value ***\n')
