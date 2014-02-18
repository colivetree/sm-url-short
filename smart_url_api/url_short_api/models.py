from django.db import models
from datetime import datetime
from smart_url_api import settings

class ShortenedURLManager(models.Manager):
    def get_new_shortened_url(self,id):
        base_URL = settings.CURRENT_BASE_URL
        
        dict_length = len(settings.SHORTENING_DICTIONARY)
        dict = settings.SHORTENING_DICTIONARY
        print dict_length
        curr_hash = ""
        #generate hash from id
        while id > 0:
            curr_letter_index = id % dict_length
            curr_hash += dict[curr_letter_index-1]
            id /= dict_length
        
        return (base_URL+curr_hash,curr_hash)





class ShortenedURL(models.Model):
    id = models.AutoField(primary_key=True)
    full_URL = models.TextField(unique=True)
    short_URL = models.TextField(unique=True)
    hash = models.TextField(unique=True)
    objects = ShortenedURLManager()

class URLAccess(models.Model):
    shortened_url = models.ForeignKey(ShortenedURL)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)
    client_IP = models.TextField()
    user_agent = models.TextField()

