from django.db import models


# Create your models here.

class shop(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, null=True)
    type = models.CharField(max_length=32, null=True)
    area = models.FloatField(max_length=32, null=True)
    boss = models.CharField(max_length=32, null=True)


class employee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, null=True)
    sex = models.CharField(max_length=32, null=True)
    age = models.CharField(max_length=32, null=True)
    createTime = models.DateTimeField(null=True)
    salary = models.CharField(max_length=32, null=True)
    shopId = models.IntegerField(null=True)


class goods(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, null=True)
    type = models.CharField(max_length=32, null=True)
    sum = models.IntegerField(null=True)
    price = models.CharField(max_length=32, null=True)
    per = models.CharField(max_length=32, null=True)
    shopId = models.IntegerField(null=True)
