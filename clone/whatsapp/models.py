from django.db import models
from django.contrib.auth.models import User

class Photos(models.Model):
    # upload your photo here
    photo=models.FileField(upload_to="photos/",default=None,null=True)
    user = models.ForeignKey(User, unique=True,on_delete=models.CASCADE,null=True)
    # user = models.ForeignKey(User, )

class User(models.Model):
    photo=models.FileField(upload_to="photos/",default=None,null=True)


class Chat(models.Model):
    
    chatcontent=models.CharField(max_length=500)
    groupname=models.ForeignKey('USerGroup',on_delete=models.CASCADE)
    username=models.CharField(max_length=200,null=True)
    
    
    

class UserGroup(models.Model):
    usergroupname=models.CharField(max_length=250,unique=True)    
        
    