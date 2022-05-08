from django.db import models

# Create your models here.

class LoginAccount(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.TextField(max_length=30)
    last_name = models.TextField(max_length=30)
    email = models.CharField(max_length=60)
    contact_no = models.IntegerField()
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    date_joined	= models.DateTimeField(verbose_name='date joined',auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login',auto_now=True)

    class Meta:
        db_table = 'login_account'


class SendMsg(models.Model):
    contact_no = models.CharField(max_length=12)
    message = models.CharField(max_length=10000)
    time_hour = models.IntegerField()
    time_min = models.IntegerField()
    wait_time = models.IntegerField()

    class Meta:
        db_table = 'send_msg'



class Sendimg(models.Model):
    receiver = models.CharField(max_length=100)
    image_path = models.CharField(max_length=1000)
    caption = models.CharField(max_length=10000)

    class Meta:
        db_table = 'send_image'


class text_to_handwritten(models.Model):
    text = models.CharField(max_length=10000)
    save_to_image_path = models.CharField(max_length=1000)

    class Meta:
        db_table = 'text_to_handwritten'


class send_mail(models.Model):
    sender_email = models.CharField(max_length=60)
    password = models.CharField(max_length=100)
    subject = models.CharField(max_length=1000)
    message = models.CharField(max_length=10000)
    receiver_email = models.CharField(max_length=60)

    class Meta:
        db_table = 'send_mail'


class play_youtube(models.Model):
    topic = models.CharField(max_length=60)
    open_video = models.BooleanField()

    class Meta:
        db_table = 'play_youtube'

