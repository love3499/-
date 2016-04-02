from django.db import models
from django.conf import settings
# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 30)
    tag = models.CharField(max_length = 30)
    headImg = models.FileField(upload_to = './/')

    def __str__(self):
        return self.username
    # def __str__(self):
    	# return '%s %s %s' % (self.username, self.tag,self.headImg)
    # def __userHeadImg__(self):
        # return self.headImg
    # def __tag__(self):
        # return self.tag
# Create your models here.
