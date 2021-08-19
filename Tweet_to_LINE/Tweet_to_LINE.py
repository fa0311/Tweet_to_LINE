
import tweepy
import time
import sys
import calendar
import requests
import time
import re

class Tweet_to_LINE:
    def __init__(self, twitter_client, wait = 60 * 5):
        self.twitter_client = twitter_client
        self.wait = wait
        self.twitter_api = tweepy.API(self.twitter_client, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)
        self.tweets = []

    def get_tweets(self,id):
        self.tweets.extend(self.twitter_api.user_timeline(id=id, count=15, include_rts=False, exclude_replies= True))
        return Tweet_to_LINE_Trim(self)

    def send(self, line_notify_token):
        for tweets in self.tweets:
            if time.time() < self.created_at(str(tweets.created_at)) + self.wait:
                output = tweets.user.name + "\n"
                output += tweets.text + "\n"
                output += "https://twitter.com/" + tweets.user.screen_name + "/status/" + tweets.id_str
                self.send_notify(output,line_notify_token)

    def created_at(self,created):
        time_utc = time.strptime(created, '%Y-%m-%d %H:%M:%S')
        return calendar.timegm(time_utc)

    def send_notify(self,notification_message,line_notify_token):
        line_notify_api = 'https://notify-api.line.me/api/notify'
        headers = {'Authorization': f'Bearer {line_notify_token}'}
        data = {'message': f'{notification_message}'}
        requests.post(line_notify_api, headers=headers, data=data)

    def print(self):
        for tweets in self.tweets:
            if time.time() < self.created_at(str(tweets.created_at)) + self.wait:
                print(tweets.text)


class Tweet_to_LINE_Trim:
    
    def __init__(self,tweets):
        self.tweets = tweets

    def trim(self,regex,flag):
        output = []
        for tweets in self.tweets.tweets:
            if (re.search(regex, tweets.text) == None) == flag:
                output.append(tweets)
        self.tweets.tweets = output
        return Tweet_to_LINE_Trim(self.tweets)


