import os
from dotenv import load_dotenv, dotenv_values 
from ytmusicapi import YTMusic, OAuthCredentials
load_dotenv() 

# Init YTM with OAUTH credentials
YTM_CLIENT_ID = os.getenv("YTM_CLIENT_ID")
YTM_CLIENT_SECRET= os.getenv("YTM_CLIENT_SECRET")
yt = YTMusic(
  "oauth.json",
  oauth_credentials=OAuthCredentials(
    client_id=YTM_CLIENT_ID,
    client_secret=YTM_CLIENT_SECRET
  )
)

# yt = YTMusic('oauth.json')
search_results = yt.search('Oasis Wonderwall')
print(search_results)
# print(YTM_CLIENT_ID)
# ytmusic.get_history()