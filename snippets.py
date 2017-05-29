from tweepy import TweepError
import time

def retry(method):
    try:
        return method()
    except TweepError as err:
        if err.message[0]['code'] == 88:
            time.sleep(60)
            return method()
