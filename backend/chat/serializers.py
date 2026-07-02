from rest_framework import serializers
from .models import FAQResponse

# Serializer for the FAQResponse model
# This serializer converts the FAQResponse model instances into JSON format and vice versa.
class FAQResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQResponse
        fields = ['id', 'question', 'answer', 'category', 'created_at'] 

