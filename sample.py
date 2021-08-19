import tweepy

from Tweet_to_LINE import Tweet_to_LINE


if __name__ == "__main__":
    twitter_client = tweepy.OAuthHandler("xxxxxxxxxxxxxxxxxxxx","xxxxxxxxxxxxxxxxxxxx")
    twitter_client.set_access_token("xxxxxxxxxxxxxxxxxxxx", 'xxxxxxxxxxxxxxxxxxxx')
    line_notify_token = "xxxxxxxxxxxxxxxxxxxxxxx"

    alert = Tweet_to_LINE.Tweet_to_LINE(twitter_client)
    alert.get_tweets("priconne_redive")
    alert.send(line_notify_token)

    alert = Tweet_to_LINE.Tweet_to_LINE(twitter_client)
    alert.get_tweets("gigazine").trim(r"\([0-9]{4}\)",True)
    alert.send(line_notify_token)

    alert = Tweet_to_LINE.Tweet_to_LINE(twitter_client)
    alert.get_tweets("livedoornews").trim(r"[0-9]{4,}RT",True)
    alert.send(line_notify_token)