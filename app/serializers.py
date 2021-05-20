
from rest_framework import serializers
from app.models import Short
class URLSerializer(serializers.ModelSerializer):
    # url=serializers.CharField(max_length=64)
    # shortcode=serializers.CharField(max_length=64)
    # def create(self,validated_data):
    #     return Short.objects.create(**validated_data)
    class Meta:
        model=Short
        fields='__all__'
