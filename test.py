# import requests
# import base64
# AUTH_URL = 'https://accounts.spotify.com/authorize'
# TOKEN_URL = 'https://accounts.spotify.com/api/token'
# BASE_URL = 'https://api.spotify.com/v1/'
# CLIENT_ID = '76c57350098e47e19eab6a4f50782348'
# CLIENT_SECRET = 'c98eed161a6c434ca3e4b0d080de5c8a'


# # Make a request to the /authorize endpoint to get an authorization code
# auth_code = requests.get(AUTH_URL, {
#     'client_id': CLIENT_ID,
#     'response_type': 'code',
#     'redirect_uri': 'https://open.spotify.com/collection/playlists',
#     'scope': 'user-modify-playback-state',
# })

# print(auth_code.text)

# auth_header = base64.urlsafe_b64encode(
#     (CLIENT_ID + ':' + CLIENT_SECRET).encode())
    
# headers = {
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Authorization': 'Basic %s' % auth_header.decode()
# }

# payload = {
#     'grant_type': 'authorization_code',
#     'code': auth_code,
#     'redirect_uri': 'https://open.spotify.com/collection/playlists',
#     'client_id': CLIENT_ID,
#     'client_secret': CLIENT_SECRET,
# }

# # Make a request to the /token endpoint to get an access token
# access_token_request = requests.post(
#     url=TOKEN_URL, data=payload, headers=headers)

# # convert the response to JSON
# access_token_response_data = access_token_request.json()

# print(access_token_response_data)

# # save the access token
# access_token = access_token_response_data['access_token']


# import requests

# CLIENT_ID = '76c57350098e47e19eab6a4f50782348'
# CLIENT_SECRET = 'c98eed161a6c434ca3e4b0d080de5c8a'

# AUTH_URL = 'https://accounts.spotify.com/api/token'

# # POST
# auth_response = requests.post(AUTH_URL, {
#     'grant_type': 'client_credentials',
#     'client_id': CLIENT_ID,
#     'client_secret': CLIENT_SECRET,
# })

# # convert the response to JSON
# auth_response_data = auth_response.json()

# # save the access token
# access_token = auth_response_data['access_token']

# print(access_token)


import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from time import sleep
import os

os.environ["SPOTIPY_CLIENT_ID"] = '76c57350098e47e19eab6a4f50782348'
os.environ["SPOTIPY_CLIENT_SECRET"] = 'c98eed161a6c434ca3e4b0d080de5c8a'
os.environ["SPOTIPY_REDIRECT_URI"] = 'http://localhost'

scope = "user-read-playback-state,user-modify-playback-state"

sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(scope=scope))

# Shows playing devices
res = sp.devices()
pprint(res)

# Change volume
sp.volume(100)
sleep(5)
sp.volume(50)
sleep(5)
sp.volume(100)