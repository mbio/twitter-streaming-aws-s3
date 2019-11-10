import configparser
import json
import tweepy


config = configparser.ConfigParser()
config.read('config.ini')

twitter_api_key = config['twitter']['api_key']
twitter_api_secret_key = config['twitter']['api_secret_key']
twitter_access_token = config['twitter']['access_token']
twitter_access_token_secret = config['twitter']['access_token_secret']
twitter_keywords = [x.strip() for x in config['twitter']['stream_keywords'].split(',') if x != '']


class TwitterStreamListener(tweepy.StreamListener):
    
    def on_data(self, data):
        raw_data = json.loads(data)
        print(raw_data)
        #print(raw_data['user']['screen_name'])

    def on_error(self, status_code):
        print('Error status code: ', status_code)
        return False


twitter_oauth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret_key)
twitter_oauth.set_access_token(twitter_access_token, twitter_access_token_secret)
twitter_api = tweepy.API(twitter_oauth)
twitter_stream = tweepy.Stream(auth=twitter_api.auth, listener=TwitterStreamListener())


try:
    print('Streaming started...')

    if len(twitter_keywords):
        twitter_stream.filter(track=twitter_keywords)
    else:
        twitter_stream.sample()

except KeyboardInterrupt as e:
    print('Streaming stopped.')

finally:
    print('Application closed.')
    twitter_stream.disconnect()
