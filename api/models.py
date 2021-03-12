from django.db import models

class MetaUser(models.Model):
    """User for api."""
    name = models.CharField(max_length = 100)
    phone = models.CharField(primary_key = True,max_length = 10)
    is_online = models.BooleanField()
    pass_date = models.CharField(max_length=100)
    balance = models.IntegerField()
    def __str__(self):
        return self.name + ' Телефон: ' + self.phone

class Driver(MetaUser):
    """User for api Driver."""
    x = models.FloatField()
    y = models.FloatField()

class Advertiser(MetaUser):
    """User for api Advertiser."""
    class TarChoises(models.IntegerChoices):
        NO_TAR = 0
        FIRST_TAR = 1
        SECOND_TAR = 2
        THIRD_TAR = 3

    tarif = models.IntegerField(choices=TarChoises.choices, default=0)
    company = models.CharField(max_length=30, default='None')

"""Работа с чатом"""
class Chat(models.Model):
    user = models.ForeignKey(MetaUser, on_delete=models.CASCADE)

    def __str__(self):
        return 'Чат c ' + self.user.__str__()

class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.CharField(max_length=10)
    date =  models.DateField().auto_now_add
    text = models.TextField(max_length=1000,default='Lorem Ipsum')

"""Работа с картинками и видео"""
class Image(models.Model):
    user = models.ForeignKey(MetaUser, on_delete=models.CASCADE)
    itype = models.CharField(max_length=5, default='pass')
    img = models.ImageField(upload_to='UserImages/')