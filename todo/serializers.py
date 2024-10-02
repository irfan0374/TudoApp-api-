from django.contrib.auth.models import User
from .models import Todo
from django.contrib.auth import authenticate
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(write_only=True,required=True)
    class Meta:
        model=User
        fields=['id','username','email','password','password2']
        extra_kwargs={
            'email':{'required':True}
        }

    def save(self,**kwargs):
        account=User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],

        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"password":"is not matching"})
        account.set_password(password)
        account.save()
        return account
    

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'task', 'status', 'created_date','user']
        extra_kwargs={
            "task":{"required":True},
            "user":{"read_only":True}
        }

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields=[
            'id','task','status','created_date',
        ]
        extra_kwargs={
            "task":{"read_only":True}
        }
