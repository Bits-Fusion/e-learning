# rest frame work imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import (
	BasePermission, 
	IsAuthenticatedOrReadOnly,
	IsAuthenticated
	)

# django imports
from django.contrib.auth import authenticate, login, logout


# project imports
from .models import AuthUserModel as User
from .validate_password import validate_password
from .serializer import UserSerializer


class UserLoginView(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            return Response({'message':'already is authenticated'})
        email = request.data.get('email')
        username = request.data.get('user_name')
        password = request.data.get('password')
        print(request)
        user = authenticate(email=email, username=username, password=password)
        if user:
            login(request, user)
            return Response({'message': 'Login successful'})
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        

class UserSignUpView(APIView):
    def permission_denied(self, request, message=None, code=None):
        pass


    def post(self, request):
        email = request.data.get('email')
        username = request.data.get('user_name')
        first_name = request.data.get('firstname')
        password = request.data.get('password')
        password2 = request.data.get('password2')
        if password2 != password:
            return Response({'message': 'unmatch password'})
        elif User.objects.filter(email=email).exists():
            return Response({'message': 'User with the same email was found'})
        elif User.objects.filter(user_name=username).exists():
            return Response({'message': 'User with the same user name was found'})
        else:
            temp = validate_password(password)
            messages = {}
            if temp:
                for j, i in enumerate(temp):
                    messages[f'error {j}'] = i
                return Response(messages)
            else:
                User.objects.create_user(
                    email = email,
                    user_name = username,
                    first_name = first_name,
                    password = password,
                    is_active = True,
                )

        return Response({'message': 'account created'})


class UserLogOut(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            logout(request)
            return Response({'message': 'Loged Out'})
        return Response({'message': 'user is not loged in'})
            

class ProfileUpdate(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            instant = User.objects.get(user_name=request.user)
            username = request.data.get('user_name')
            password = request.data.get('password')
            temp = validate_password(password)
            messages = {}
            if temp:
                for j, i in enumerate(temp):
                    messages[f'password requirment {j}'] = i
                return Response(messages)

            instant.user_name = username
            instant.set_password(password)
            instant.save()

            return Response({'masseage':'updated successful'})


@permission_classes([IsAuthenticated])
class ProfileDamp(generics.ListAPIView):
	permission_classes = [IsAuthenticated] 
	queryset = User.objects.all()
	serializer_class = UserSerializer
	lookup_field = 'user_name'