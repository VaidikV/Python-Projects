from speedtest import Speedtest
from twitter import Twitter

PROMISED_DOWN = 100
PROMISED_UP = 100

speedtest = Speedtest()
speedtest.get_internet_speed()
down_speed = speedtest.down
up_speed = speedtest.up
# print(float(down_speed))
# print(up_speed)

if float(down_speed) < PROMISED_DOWN and float(up_speed) < PROMISED_UP:
    print("Tweeting at provider")
    twitter = Twitter(down_speed, up_speed)
    twitter.tweet_at_provider()
else:
    print("Optimal download and upload speeds")
