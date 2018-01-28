"""
Twitter search handler for @johnkntran.

This file goes where your backend scripts are being served, such as 
/Library/WebServer/CGI-Executables on a Mac, or /var/www/wsgi-scripts on CentOS.
"""

import collections
import traceback
import tweepy
import config
import utils
import webob
import json
import sys
import os


# Consumer keys and access tokens for OAUTH 1.0 for my @johnkntran account - 
#   normally store these in a database or somewhere that's protected.
#   I won't set up a database instance for this example, but you should for 
#   a real production app. Can be as simple as SQLite or something. Please 
#   don't abuse my Twitter tokens.
consumer_key = "KMtKN5XHNiDxCI5s6ELv5vGXF"
consumer_secret = "T0T4fXCx64i8Oh5wtHF4DVeZ2cFDTJKqZc6YS2ueDGNYq8ZY4u"
access_token = "4830201730-5ubQe0muCHtC8TuIsH9OrQVeHIcpCajIKdITqlf"
access_secret = "GXWcWdwpkBQcLhVGdxqQlWm2MJG9InXxz4YyublbrcviL"
access_level = "Read and write"
owner = "johnkntran"
owner_id = "4830201730"


def application(environ, start_response):
    # Set up initial parameters and utility instances
    request = webob.Request(environ)
    params = json.loads(request.body) if request.body else {'username': 'interior'} # Default to USDI
    utl = utils.util(environ, start_response)

    try:

        # Authorize the Twitter API `auth` object using OAuth tokens
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)

        # Set the `auth` object for tweepy's API
        twitter_api = tweepy.API(auth)

        # Perform a search
        ## tweets = twitter_api.search(q='from%3A{usernm}%20OR%20%23{usernm}%20OR%20%40{usernm}'
        ##    .format(usernm=params['username'])) # from:nasa OR #nasa OR @nasa
        tweets = twitter_api.search(q='from%3A{usernm}'.format(
            usernm=params['username'])) # from:interior

        # Iterate over first 5 tweets and add information to response payload
        payload = []
        for tweet in tweets[:5]:
            tweet_props = {
                "text": tweet.text, # Tweet contents
                "time": tweet.created_at.strftime("%-m/%-d/%y at %I:%M %p"), # Datetime formatted
                "num_words": len(tweet.text.split()) # Number of words in content split by whitespace
            }
            payload.append(tweet_props)

        # Log a successful result
        res = True

    except Exception as e:
        res = False
        err_texts = []
        excptn, err_msg, tb = sys.exc_info()
        for file_name, line_no, func_name, text in traceback.extract_tb(tb):
            err_text = '{} (LINE {}) in {}() -> `{}`'.format(
                os.path.basename(file_name), line_no, func_name, text)
            err_texts.append(err_text)
        err_texts.insert(0, '{} {}'.format(e.message, type(e)))
        tb_error = '\n'.join(err_texts)

    finally:
        data = collections.OrderedDict()
        data['result'] = str(res)
        data['traceback'] = tb_error if not res else None # Comment out in production
        if res:
            data['payload'] = payload
        resp = json.dumps(data)
        return utl.send_data(resp)
