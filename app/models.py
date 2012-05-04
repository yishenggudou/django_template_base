# -*- coding:utf-8 -*-
# Create your models here.
from django.db import models





class Invite(models.Model):
    u"""
    """
    #id = models.CharField(u'User ID',max_length=200,unique=True,primary_key=True)
    id = models.AutoField(primary_key=True)  
    email = models.CharField(u'email',max_length=100)
    code = models.CharField(u'code',max_length=32)
    is_used = models.BooleanField(u'if has used',default=False)


class Apply(models.Model):
    u"""
    """
    id = models.AutoField(primary_key=True)  
    email = models.CharField(u'email',max_length=200)
    name = models.CharField(u'name',max_length=200)
    message = models.CharField(u'massage',max_length=200)
    apply_time = models.DateTimeField(auto_now_add=True)


