
from rest_framework import serializers
from .models import UserDetails


class UseSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserDetails
        fields = ['username','password','date_of_birth','email','mobile_number','profile_picture']
        extra_kwargs = { 
            'password':{'write_only':True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password',None)
        
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password('password')
        instance.save()
        return instance

