
from rest_framework import serializers
from publishers.models import Publishers

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publishers
        fields = ['id','name','address','contact_email']