import tweepy


#Tweet Part : collect past 20 tweets via the twitter api with help from tweepy
# write your key and secret
consumer_key = 'RASWKDC5cbzlJAdXVkQ65wNNf'
consumer_secret = 'Z0EmrLswOFxCyyDzp7u7spu1Qq7h5kJ9jsztW2btJ4BdgrJJuy'
oauth_token = '24994596-U32WhPf4Xi7YaKIY77G9Jg1kXDQCoU90n4ZGzMsr4'
oauth_token_secret = '0EGYYiKiIeiQOBOyQDqhMvUEghXNiQoqfjpmCf3yIurpT'

# create Api instance
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(oauth_token, oauth_token_secret)
api = tweepy.API(auth)

def search_tweets():
    return api.user_timeline(count=20, screen_name = "tkloumo", trim_user=True, include_rts=False)

def fav_tweet(tweet):
    print tweet.id
    try:
      api.create_favorite(tweet.id)
      return
    except:
      return


def main():
    result = search_tweets()
    for tweet in result:
      print tweet.text
    success = 0
    for tweet in result:
        fav_tweet(tweet)


