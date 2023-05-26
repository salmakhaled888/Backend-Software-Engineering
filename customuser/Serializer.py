from rest_framework import serializers
from customuser import models

class UserSerializer(serializers.ModelSerializer):
    password=serializers.CharField(
        write_only=True
    )

    class Meta:
        model=models.CustomUser
        fields=['id','name','email','password']
    def create(self, validated_data):
        user=models.CustomUser.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password=validated_data.pop()
            instance.set_passowrd(password)
        return super.update(instance, validated_data)