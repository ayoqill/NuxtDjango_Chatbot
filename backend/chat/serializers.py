from rest_framework import serializers
from .models import FAQResponse
from django.contrib.auth.models import User

# Serializer for the FAQResponse model
# This serializer converts the FAQResponse model instances into JSON format and vice versa.
class FAQResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQResponse
        fields = ['id', 'question', 'answer', 'category', 'created_at'] 


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password']
        )
        return user
    
#   How this works?
#           
#   username, email, password
#           ↓
#   Django creates a new user
#           ↓
#   Password is safely hashed
#
#  
#   This is better than User.objects.create(...) because it encrypts the password.
