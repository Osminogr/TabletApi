from rest_framework import serializers
from .models import Driver, Advertiser

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 100)
    phone = serializers.CharField(max_length = 10)
    is_online = serializers.BooleanField()
    pass_date = serializers.CharField(max_length=100)
    balance = serializers.IntegerField()

    def create(self, validated_data):
        return MUser.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.is_online = validated_data.get('is_online', instance.is_online)
        instance.is_driver = validated_data.get('is_driver', instance.is_driver)
        instance.card = validated_data.get('card', instance.card)
        instance.cvv = validated_data.get('cvv', instance.cvv)
        instance.carddate = validated_data.get('carddate', instance.carddate)
        instance.x = validated_data.get('x', instance.x)
        instance.y = validated_data.get('y', instance.y)
        instance.pass_date = validated_data.get('pass_date', instance.pass_date)
        instance.balance = validated_data.get('balance', instance.balance)
        instance.company = validated_data.get('company', instance.company)
        instance.save()
        return instance

class DriverSerializer(UserSerializer):
    x = serializers.FloatField()
    y = serializers.FloatField()

    def create(self, validated_data):
        return Driver.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.is_online = validated_data.get('is_online', instance.is_online)
        instance.x = validated_data.get('x', instance.x)
        instance.y = validated_data.get('y', instance.y)
        instance.pass_date = validated_data.get('pass_date', instance.pass_date)
        instance.balance = validated_data.get('balance', instance.balance)
        instance.save()
        return instance
    

class AdvertiserSerialiser(UserSerializer):
    tarif = serializers.IntegerField()
    company = serializers.CharField(max_length = 30)

    def create(self, validated_data):
        return Advertiser.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.is_online = validated_data.get('is_online', instance.is_online)
        instance.pass_date = validated_data.get('pass_date', instance.pass_date)
        instance.balance = validated_data.get('balance', instance.balance)
        instance.company = validated_data.get('company', instance.company)
        instance.save()
        return instance
    
    
