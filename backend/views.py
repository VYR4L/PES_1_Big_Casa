from django import http
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.contrib.auth import authenticate
from .models import Usuario


class Login(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('cpf')
        password = request.data.get('password')

        if not username or not password:
            return Response(
                {'message': 'Username and password are required'},
                status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = Usuario.objects.get(username=username)
        except:
            user = None

        if user and user.check_password(password):
            return Response({
                'message': 'Login successful'},
                status=status.HTTP_200_OK
            )
        else:
            return Response({
                'message': 'Invalid credentials'},
                status=status.HTTP_401_UNAUTHORIZED
                )
        

class Create_user(APIView):
    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone')
        cpf = request.data.get('cpf')
        adress = request.data.get('adress')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        password = request.data.get('password')

        if not first_name or not last_name or not phone or not cpf or not adress or not first_name or not last_name or not password:
            return Response({
                'message': 'All fields are required'},
                status=status.HTTP_400_BAD_REQUEST)
        
        if Usuario.objects.filter(cpf=cpf).exists():
            return Response({
                'message': 'CPF already exists'},
                status=status.HTTP_400_BAD_REQUEST)
        
        user = Usuario.objects.create_user(first_name=first_name, last_name=last_name, adress=adress, password=password)

        if user:
            return Response({
                'message': 'User created'},
                status=status.HTTP_201_CREATED)
        else:
            return Response({
                'message': 'Failed to create user'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
