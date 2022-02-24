from rest_framework import serializers
from .models import Articale


class ArticaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articale
        # fields = ['id', 'title', 'author', 'email']
        fields = '__all__'
