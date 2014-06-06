import tweepy


#Tweet Part : collect past 20 tweets via the twitter api with help from tweepy
# write your key and secret
consumer_key = 'your '
consumer_secret = 'keys'
oauth_token = 'placed'
oauth_token_secret = 'here'

# create Api instance
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(oauth_token, oauth_token_secret)
api = tweepy.API(auth)

def search_tweets():
    return api.user_timeline(count=20, screen_name = "tkloumo", trim_user=True, include_rts=False)

def fav_tweet(tweet):
    try:
      api.create_favorite(tweet.id)
      return
    except:
      return


def main():
    result = search_tweets()
    for tweet in result:
        fav_tweet(tweet)


