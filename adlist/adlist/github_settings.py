# Copy this file to github_settings.py (don't check it into github)

# Go to https://github.com/settings/developers

# Add a New OAuth2 App - GIve it a name

# If you are running on localhost, make the callback url be
# http://127.0.0.1:8000/oauth/complete/github/

# If you are on the real internet (or using ngrok) make the callback url be
# https://samples.dj4e.com/oauth/complete/github/

# Then copy the client_key and secret to this file

SOCIAL_AUTH_GITHUB_KEY = 'c1c342adb0cb647d34ef'
SOCIAL_AUTH_GITHUB_SECRET = 'a962f1a84245e6c71a2420d8a325b0549cd30090'