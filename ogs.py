import json
import requests

'''
private_client.py contains a dictionary called data that contains important client information:
client_id
client_secret
grant_type
username
password
'''
import private_client

def bytes_to_dict(req):
    return json.loads(str(req.content,'utf-8'))

oauth_req = requests.post('https://online-go.com/oauth2/access_token', data=private_client.data)
oauth_token = bytes_to_dict(oauth_req)

headers = {
    "Authorization": "Bearer " + oauth_token["access_token"]
}

stats_req = requests.get('https://online-go.com/api/v1/me/', headers=headers)
stats = bytes_to_dict(stats_req);
print(stats)
