from rest_framework import serializers
from .models import Merch

class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merch
        fields = ('id', 'name', 'price', 'description', 'created_at')

