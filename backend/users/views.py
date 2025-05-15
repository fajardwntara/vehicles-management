from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import status
from django.shortcuts import get_object_or_404

from .permissions import IsAdmin
from .serializers import (
    UserSerializer, 
    UserCreateSerializer, 
    UserUpdateSerializer, 
    TokenObtainSerializer,
)

User = get_user_model()

class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        """ return all of users """
        try:
            users = [{
                "id": user.id,
                "username": user.username,
                "role": user.role,
                "email": user.email
            } for user in User.objects.all()]

            return Response(users, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(
                {"error": f"{str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk, format=None):
        """ return one user request """
        try:
            users = [{
                "username": user.username,
                "role": user.role,
                "email": user.email
            } for user in User.objects.filter(id=pk)]

            return Response(users, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {"error": f"{str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class UserCreateView(APIView):
    """ create a new user """
    permission_classes = [IsAdmin]

    def post(self, request, format=None):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "User created successfully",
                "user": {
                    "username": user.username,
                    "email": user.email,
                    "role": user.role,
                }
            }, status=status.HTTP_201_CREATED)
            
        return Response({
            "error": [serializer.errors[error][0] for error in serializer.errors]
        }, status=status.HTTP_400_BAD_REQUEST)

class UserUpdateView(APIView):
    """ update a user """
    permission_classes = [IsAdmin]

    def put(self, request, pk, format=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserUpdateSerializer(user, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "User updated successfully",
                "user": serializer.data
            }, status=status.HTTP_200_OK)
        
        return Response({
            "error": [serializer.errors[error][0] for error in serializer.errors]
        }, status=status.HTTP_400_BAD_REQUEST)

class UserDeleteView(APIView):
    """ delete a user """
    
    permission_classes = [IsAdmin]

    def delete(self, request, pk, format=None):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response({
            "message": "User deleted successfully"
        }, status=status.HTTP_204_NO_CONTENT)

# Obtaining token
class TokenObtainPair(TokenObtainPairView):
    """ obtain token to user """
    serializer_class = TokenObtainSerializer