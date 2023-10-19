from django.contrib.auth.models import User
from .models import Contact, RawContact, Lead
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields ='__all__'

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'

    def validate(self, attrs):
        attrs[self.username_field] = attrs.get(self.username_field).lower()
        return super().validate(attrs)
    

class RawContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawContact
        fields = '__all__'

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'