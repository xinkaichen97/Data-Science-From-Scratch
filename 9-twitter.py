from collections import Counter
from twython import Twython, TwythonStreamer
import json

credentials = """{"API_KEY" : "tyiznD1a3sFX67yMonlFiwhie", 
"API_SECRET_KEY" : "ZUhCOBjvMZRslhsj59oSD5rF0JdANNsHgpglXmK4HfUFvN4CfQ",
"ACCESS_TOKEN" : "840821375581507584-sny08HSvtHKc4wjelNH5QoLpkst7O4i",
"ACCESS_TOKEN_SECRET" : "NtiwkR1cOjndF2Wgvv13C6uOtjq2AMtq8W2wXP8c0OYTW"}"""

info = json.loads(credentials)
API_KEY = info["API_KEY"]
API_SECRET_KEY = info["API_SECRET_KEY"]
ACCESS_TOKEN = info["ACCESS_TOKEN"]
ACCESS_TOKEN_SECRET = info["ACCESS_TOKEN_SECRET"]

# print(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

twitter = Twython(API_KEY, API_SECRET_KEY)
for status in twitter.search(q='"data science"')["statuses"]:
    user = status["user"]["screen_name"]
    text = status["text"]
    print(user, ':', text)
    print()

tweets = []


class MyStreamer(TwythonStreamer):

    def on_success(self, data):
        if data['lang'] == 'en':
            tweets.append(data)
            print('Received Tweet #', len(tweets))
            print(data['user']['name'], ':', data['text'])
            print()
        if len(tweets) >= 20:
            self.disconnect()

    def on_error(self, status_code, data):
        print(status_code, data)
        self.disconnect()


stream = MyStreamer(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
stream.statuses.filter(track='data')
top_hashtags = Counter(hashtag['text'].lower() for tweet in tweets for hashtag in tweet["entities"]["hashtags"])
print(top_hashtags.most_common(5))
