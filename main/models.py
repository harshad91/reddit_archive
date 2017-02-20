from __future__ import unicode_literals

from django.db import models
from mongoengine import *


class Submission(Document):
    subreddit = StringField(required=True)
    title = StringField()
    permalink = StringField()
    ups = IntField()
    created_utc = DateTimeField()
    num_comments = IntField()


class CurrentPointer(Document):
    subreddit = StringField(required=True)
    year = IntField()
    created_utc = DateTimeField()
