

from rest_framework import serializers
from authers.models import Authors


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authors
        fields = ['id','name','biography']

        