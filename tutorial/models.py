from __future__ import unicode_literals

from django.db import models
import datetime


class Video(models.Model):
    title = models.CharField(max_length=200, unique=True)
    youtube_id = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField(max_length=800, blank=True, null=True)
    date = models.DateTimeField(default=datetime.datetime.now())

    def __unicode__(self):
        return self.title


class Tutorial(models.Model):
    title = models.CharField(max_length=200, unique=True)
    videos = models.ManyToManyField(Video)
    description = models.TextField(max_length=800, blank=True, null=True)
    similar = models.ManyToManyField("self", null=True, blank=True)
    date = models.DateTimeField(default=datetime.datetime.now())

    def __unicode__(self):
        return self.title
