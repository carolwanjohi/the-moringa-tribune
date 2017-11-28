from rest_framework import serializers
from .models import MoringaMerch

class MerchSerializer(serializers.ModelSerializer):
    '''
    Convert MoringaMerch model to JSON
    '''
    class Meta:
        model = MoringaMerch
        fields = ('name', 'description', 'price')
