from rest_framework import serializers
from .models import MUser

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 100)
    phone = serializers.CharField(max_length = 10)
    is_online = serializers.BooleanField()
    is_driver = serializers.BooleanField()
    card = serializers.CharField(max_length = 16)
    cvv = serializers.CharField(max_length = 3)
    carddate = serializers.CharField(max_length=4)
    x = serializers.FloatField()
    y = serializers.FloatField()
    pass_date = serializers.CharField(max_length=100)
    balance = serializers.IntegerField()
    company = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return MUser.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instanse.name)
        instance.phone = validated_data.get('phone', instanse.phone)
        instance.is_online = validated_data.get('is_online', instanse.is_online)
        instance.is_driver = validated_data.get('is_driver', instanse.is_driver)
        instance.card = validated_data.get('card', instanse.card)
        instance.cvv = validated_data.get('cvv', instanse.cvv)
        instance.carddate = validated_data.get('carddate', instanse.carddate)
        instance.x = validated_data.get('x', instanse.x)
        instance.y = validated_data.get('y', instanse.y)
        instance.pass_date = validated_data.get('pass_date', instanse.pass_date)
        instance.balance = validated_data.get('balance', instanse.balance)
        instance.company = validated_data.get('company', instanse.company)
        instance.save()
        return instance