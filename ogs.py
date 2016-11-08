import json
import requests

import private_client

r = requests.post('https://online-go.com/oauth2/access_token', data=private_client.data)

headers = {
    "Authorization": "Bearer " + json.loads(str(r.content,'utf-8'))["access_token"]
}

friends = requests.get('https://online-go.com/api/v1/me/friends', headers=headers)
print(friends.content)
