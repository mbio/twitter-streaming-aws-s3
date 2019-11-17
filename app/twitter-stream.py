import boto3
import configparser
import tweepy


class TwitterStreamListener(tweepy.StreamListener):
    
    def on_data(self, data):
        stream_tweet(data)

    def on_error(self, status_code):
        print('Error status code: ', status_code)
        return False


config = configparser.ConfigParser()
config.read('config.ini')

twitter_api_key = config['twitter']['api_key']
twitter_api_secret_key = config['twitter']['api_secret_key']
twitter_access_token = config['twitter']['access_token']
twitter_access_token_secret = config['twitter']['access_token_secret']
twitter_keywords = [x.strip() for x in config['twitter']['stream_keywords'].split(',') if x != '']

twitter_oauth = tweepy.OAuthHandler(twitter_api_key, twitter_api_secret_key)
twitter_oauth.set_access_token(twitter_access_token, twitter_access_token_secret)
twitter_api = tweepy.API(twitter_oauth)
twitter_stream = tweepy.Stream(auth=twitter_api.auth, listener=TwitterStreamListener())

aws_kinesis_stream_name = config['aws']['kinesis_stream_name']
aws_client = boto3.client(
    'firehose',
    aws_access_key_id=config['aws']['access_key_id'],
    aws_secret_access_key=config['aws']['secret_access_key'],
    region_name=config['aws']['region']
)


def stream_tweet(data):
    response = aws_client.put_record(
        DeliveryStreamName=aws_kinesis_stream_name,
        Record={
            'Data': data.encode()
        }
    )

    print(response)


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
