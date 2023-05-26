from django.shortcuts import render

from rest_framework import viewsets, filters
from rest_framework.settings import api_settings
from customuser.models import CustomUser
from .Serializer import UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from customuser.permissions import IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication



class UserViewSet(viewsets.ModelViewSet):

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsOwnerOrReadOnly]
    # authentication_classes = (TokenAuthentication,)


class LoginView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
