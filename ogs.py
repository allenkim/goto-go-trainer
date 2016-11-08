"""
Python file for various OGS API calls
"""
import json
import requests

# private_client.py contains a dictionary called data
# data has following key values:
# client_id
# client_secret
# grant_type
# username
# password
import private_client


def bytes_to_dict(req):
    """
    Returns a dictionary that is translated from a request
    Converts bytes that are in the form of dictionaries to Python dict
    Used for converting OGS API calls to data structures
    """
    return json.loads(str(req.content, 'utf-8'))


def request_ogs_token(data):
    """
    Returns a dictionary that represents an OAuth Token from OGS
    """
    oauth_req = requests.post('https://online-go.com/oauth2/access_token',
                              data=data)
    oauth_token = bytes_to_dict(oauth_req)
    return oauth_token


def request_stats(oauth_token):
    """
    Prints out the stats of the user specified in the OAuth Token
    """
    headers = {
        "Authorization": "Bearer " + oauth_token["access_token"]
    }

    stats_req = requests.get('https://online-go.com/api/v1/me/',
                             headers=headers)
    stats = bytes_to_dict(stats_req)
    print(stats)


if __name__ == "__main__":
    OAUTH_TOKEN = request_ogs_token(private_client.CLIENT_DATA)
    request_stats(OAUTH_TOKEN)
