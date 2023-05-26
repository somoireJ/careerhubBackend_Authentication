from django.http import request
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import ApplicantSignupSerializer, EmployerSignupSerializer, UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from .permissions import IsApplicantUser, IsEmployerUser


class ApplicantSignupView(generics.GenericAPIView):
    serializer_class = ApplicantSignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key,
            "message": "Account created successfully"
        })


class EmployerSignupView(generics.GenericAPIView):
    serializer_class = EmployerSignupSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key,
            "message": "Account created successfully"
        })


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        is_applicant = user.is_applicant
        is_employer = user.is_employer
 
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'is_applicant': user.is_applicant,
            'is_employer': user.is_employer,
            
        })


class LogoutView(APIView):
    def post(self, request, format=None):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)


class ApplicantOnlyView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated & IsApplicantUser]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class EmployerOnlyView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated & IsEmployerUser]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
