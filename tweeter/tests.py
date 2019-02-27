import unittest
from .serializers import TweetSerializer
from tweeter.models import Tweet
from django.contrib.auth.models import User
from datetime import datetime
from rest_framework import serializers

class TestUsers(unittest.TestCase):
    def test_user_creation(self):
        user=User(username='���')
        self.assertEqual(user.username,'���') 

        user2=User()
        self.assertEqual(user2.username,'')
    def test_user_permission(self):
        pass
        
class TestTweets(unittest.TestCase):
    def test_tweet_creation(self):
        time = datetime.now()
        tweet = Tweet(text = "Hi! I'm Bob :)", user=User(username='bob'), timestamp = time)
        self.assertEqual(tweet.text,  "Hi! I'm Bob :)")
        self.assertEqual(tweet.user.username, 'bob')
        self.assertEqual(tweet.timestamp, time)

        time = datetime(year=2010,month=10,day=10,hour=10,minute=10,second=10)
        tweet = Tweet(text = "Hi� Ý'm ßoß ձ", user=User(username='ßoß'), timestamp = time)
        self.assertEqual(tweet.text,  "Hi� Ý'm ßoß ձ")
        self.assertEqual(tweet.user.username, 'ßoß')
        self.assertEqual(tweet.timestamp, time)


    def test_serializer_validation(self):
        ts = TweetSerializer()
        self.assertRaises(serializers.ValidationError,ts.validatSe_text,"hi!")
        self.assertRaises(serializers.ValidationError,ts.validate_text," ")
        self.assertRaises(serializers.ValidationError,ts.validate_text,"  " * 71)
        self.assertEqual(ts.validate_text("  " * 70),"  "* 70)

