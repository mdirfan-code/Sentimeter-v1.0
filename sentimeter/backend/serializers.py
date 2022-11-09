from rest_framework import serializers
from .models import TwitterHash

class TwitterHashSerializer(serializers.ModelSerializer):
    class Meta:
        managed = False
        model = TwitterHash
        fields = ('hashTag')