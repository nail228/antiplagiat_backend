from django.db import models

# Create your models here.

class Deadlines(models.Model):
    dl_id = models.IntegerField(primary_key=True)
    subject = models.CharField(max_length=20)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    days = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'deadlines'

class Users(models.Model):
    user_id = models.IntegerField(primary_key=True)
    login = models.CharField(max_length=40)
    username = models.CharField(max_length=20)
    userlastname = models.CharField(max_length=20)
    deadline = models.ForeignKey(Deadlines, models.DO_NOTHING)
    password = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'users'
