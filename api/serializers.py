from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email','password']
        
    def validate(self, obj):
        if User.objects.filter(username=obj['username']).exists():
            raise serializers.ValidationError("Username already exists.")
        if User.objects.filter(email=obj['email']).exists():
            raise serializers.ValidationError("Email already exists.")
        return obj