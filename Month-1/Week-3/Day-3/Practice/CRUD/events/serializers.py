from rest_framework import serializers
from .models import Event

# Make sure 'serializers' is lowercase and 'ModelSerializer' has a capital S:
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'