from django.contrib.auth.models import User, Group
from .models import Beat
from rest_framework import serializers

#Serializer to access the 'Users' database. This is Django's built in user database
class beatserializer(serializers.ModelSerializer):
    class Meta:
        model = Beat
        fields = '__all__' #('date','room','temperature_f', humidity)

    def create(self, validated_data):
        new_beat = Beat(
            #date = datetime.datetime.now(),
            #date = validated_data['date'],
            #room = validated_data['room'],
            #temperature_f = validated_data['temperature_f'],
            #humidity = validated_data['humidity'])
            beat = validated_data['beat'])

        new_beat.save()
        return new_beat

    def update(self, instance, validated_data):
        instance.beat = validated_data.get('beat', instance.beat)

        instance.save()
        return instance
