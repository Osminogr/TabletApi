from django.db import models

class MUser(models.Model):
    """User for api MUser."""
    name = models.CharField(max_length = 100)
    phone = models.CharField(primary_key = True,max_length = 10)
    is_online = models.BooleanField()
    is_driver = models.BooleanField()
    card = models.CharField(max_length = 16)
    cvv = models.CharField(max_length = 3)
    carddate = models.CharField(max_length=4)
    x = models.FloatField()
    y = models.FloatField()
    pass_date = models.CharField(max_length=100)
    balance = models.IntegerField()
    company = models.CharField(max_length=30)

    def __str__(self):
        return self.name
        
        
