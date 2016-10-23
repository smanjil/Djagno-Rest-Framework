
from rest_framework import serializers
from .models import Stock

class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = '__all__'    #(to return all fields available in the model)
        # fields = ['ticker', 'volume']