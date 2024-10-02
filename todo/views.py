from django.shortcuts import render
from rest_framework.views import APIView

from .serializers import UserSerializer,TodoSerializer,TodoListSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken
# Create your views here.

class RegisterApiView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data["username"] = account.username
            data["email"] = account.email
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LoginApiView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        User = get_user_model()

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        
        if user.check_password(password):
            token = AccessToken.for_user(user)
            data = {
                'token': str(token), 
                'username': user.username  
            }
            return Response(data, status=status.HTTP_200_OK)
        
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


class TodoAddApiView(APIView):
    authentication_classes=(JWTAuthentication,)
    permission_classes=(IsAuthenticated,)
    def post(self ,request,*args, **kwargs):
        print("enter")
        serializer=TodoSerializer(data=request.data)
        user=request.user
        if serializer.is_valid():

            serializer.save(user=user)
            return Response(serializer.data,status=status.HTTP_201_CREATED) 
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class TodoListApiView(APIView):
    authentication_classes=(JWTAuthentication,)
    permission_classes=(IsAuthenticated,)

    def post(self,request,*args, **kwargs):
        user=request.user
        todos = user.todo_set.all()
        serializer=TodoListSerializer(todos,many=True)
        return Response(serializer.data)


class TodoDetailsApiView(APIView):
    authentication_classe=(JWTAuthentication,)
    permission_classes=(IsAuthenticated,)

    def get(self,request,*args, **kwargs):
        user=request.user
        id=kwargs.get('id')
        try:
            todos=user.todo_set.get(id=id)
            serializer=TodoListSerializer(todos)
            return Response(serializer.data)
        except:
            return Response({'message':'no such todo'})
        
    def put(self, request, *args, **kwargs):
        user = request.user
        id = kwargs.get('id')
        print(request.data)
        try:
            serializer = TodoListSerializer(data=request.data) 
            if serializer.is_valid():
                todo = user.todo_set.get(id=id)
                todo.status = serializer.validated_data['status'] 
                todo.save()
                if serializer.validated_data['status']: 
                    return Response({"message": "task completed"}, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "task is pending"}, status=status.HTTP_200_OK)
                    
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except :
            return Response({'message': 'no such todo'}, status=status.HTTP_404_NOT_FOUND)

        
    def delete(self, request, *args, **kwargs):
        user = request.user
        id = kwargs.get('id')     
        try:
            todo = user.todo_set.get(id=id)
            todo.delete()
            return Response({"message": "todo deleted"}, status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({"message": "no such todo"}, status=status.HTTP_404_NOT_FOUND)

    
