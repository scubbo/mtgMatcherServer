#!/usr/bin/python
import requests
import json

sendURL = 'https://android.googleapis.com/gcm/send'
with file('apikey','r') as f:
    apiKey = f.read().rstrip()

def buildRequest():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'key='+apiKey
    }

    with file('testRegistrationId','r') as f:
        registrationId = f.read().rstrip()
    registration_ids = [registrationId]

    data = {
        'registration_ids': registration_ids,
        'data': {
            'myFavouriteCard': 'Sliver Queen'
        }
    }

    r = requests.post(sendURL, data=json.dumps(data), headers=headers)

    print r.text

buildRequest()
