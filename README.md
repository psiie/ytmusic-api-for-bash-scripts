# How to install
1. `virtualenv venv`
2. `pip install -r requirements.txt`
3. create a browser.json by running command `ytmusicapi browser` and following steps to extract cookie from a browser session (see below section on "Login Credentials")


# How to use
1. bash into virtualenv (`source venv/bin/activate`)
2. run `python get_liked_playlist.py`
3. file "liked_songs.json" is created in "out/" directory. Errors generating this file result in a bash exit code of non-zero.

# Login Credentials
OAUTH has limitations when pertaining to Google-Family accounts. So I'm using the cookie method instead. Browser cookies could be good for 2 years.

Follow instructions at https://ytmusicapi.readthedocs.io/en/stable/setup/browser.html for browser. Keep in mind that there is a special note for MacOS pasting of cookies (for generating the browser.json file)

(As an aside, a .env file could be created for the OAUTH method if that method did work for my purposes.)