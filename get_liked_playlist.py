import json
from ytmusicapi import YTMusic, OAuthCredentials
ytmusic = YTMusic("browser.json")

# Get liked-songs playlist and format into JSON.
# Note: Limit seems to not work and instead retrieves every single like ever
liked_songs = ytmusic.get_liked_songs(limit=50) # Limit seems to not work
liked_songs_json = json.dumps(liked_songs, sort_keys=True, indent=4)

# Save as file. Return error code for use in bash scripts if failed
with open('out/liked_songs.json', 'w') as file:
  file.write(liked_songs_json)
