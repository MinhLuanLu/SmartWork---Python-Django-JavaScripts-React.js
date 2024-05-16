from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import User, Employee, Manager
from .serializers import UserSerializer
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.hashers import check_password






def home(request):
    return HttpResponse('HOME PAGE')

@api_view(['GET', 'POST'])
def register_api(request):
    if request.method == "GET":
        user = User.objects.all()
        userserializer = UserSerializer(user, many=True)
        
        return Response(userserializer.data)
    
    elif request.method == "POST":
        userserializer = UserSerializer(data=request.data)
        email = request.data.get('Email')
        role = request.data.get('Role')
            
        if User.objects.filter(Email=email).exists(): # Check the Emain is already in Database
            print("Email is already registered")
            return Response({'message': "Email is already registered"}, status=status.HTTP_400_BAD_REQUEST)
        if userserializer.is_valid():
            
            user = userserializer.save() #Save instance to User Model
            if role == "Employee":
                Employee.objects.create(user=user, Role=user.Role) # Save the instance to Employee Model
            elif role == "Manager":
                    Manager.objects.create(user=user, Role=user.Role)
            return Response({"message": "Registration successful"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Data is not valid", "error": userserializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    if request.method == "POST":
        Email = request.data.get('Email')
        Password = request.data.get('Password')
        
        user = User.objects.filter(Email=Email).first() # user first because the email is unique
        if user is None:
            raise AuthenticationFailed('User not found!')
        
        if not check_password(Password, user.Password):
            raise AuthenticationFailed('Incorrect password!')
        
        #Get the FullName in Employee
        return Response({"message": "Login successful", "FullName": user.FullName}, status=status.HTTP_200_OK)