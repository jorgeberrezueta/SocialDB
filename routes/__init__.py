from routes.auth import login as _auth_login
from routes.twitter import tweets as _twitter_tweets
from routes.twitter import profiles as _twitter_profiles

def register(app):
    _auth_login.register(app)
    _twitter_tweets.register(app)
    _twitter_profiles.register(app)