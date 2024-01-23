from rest_framework import serializers
from .models import News, CryptoCurrency

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['text', 'channel', 'currencies']

class CryproCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoCurrency
        fields = '__all__'
