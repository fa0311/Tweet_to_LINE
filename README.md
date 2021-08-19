# Tweet_to_LINE

ツイートを取得して LINEnotify で送信する<br>
<br>

## Usage

```python
import tweepy
from Tweet_to_LINE import Tweet_to_LINE

#consumer_token, consumer_secret
twitter_client = tweepy.OAuthHandler("xxxxxxxxxxxxxxxxxxxx","xxxxxxxxxxxxxxxxxxxx")
#access_token, access_token_secret 省略可
twitter_client.set_access_token("xxxxxxxxxxxxxxxxxxxx", 'xxxxxxxxxxxxxxxxxxxx')
#line_notify_token
line_notify_token = "xxxxxxxxxxxxxxxxxxxxxxx"
#cronの間隔(秒) デフォルトは300秒
wait = 60 * 5
#監視するTwitterId
account_id = "faa0311"
#インスタンス作成
alert = Tweet_to_LINE.Tweet_to_LINE(twitter_client)
#データの取得とトリム 正規表現, 結果
tweets = alert.get_tweets(account_id)
#正規表現, 結果
tweets.trim(r"TEST",False)
#コンソールに出力
alert.print(line_notify_token)
#LINEnotifyに送信
alert.send(line_notify_token)
```
