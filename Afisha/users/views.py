from django.shortcuts import get_object_or_404
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .models import ConfirmationCode
from .serializers import UserSerializer

User = get_user_model()


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save(is_active=False)  # Создаем пользователя, но он пока неактивен
            ConfirmationCode.objects.create(user=user)  # Создаем код подтверждения и привязываем его к пользователю
            return Response({"detail": "User registered. Please confirm your email."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConfirmUserView(APIView):
    permission_classes = [AllowAny]



