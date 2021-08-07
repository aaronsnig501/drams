from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import AccountSerializer


class RegisterAccount(APIView):

    permission_classes = [AllowAny]
    serializer_class = AccountSerializer

    def post(self, request, format="json"):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# from requests.exceptions import HTTPError

# from django.shortcuts import render
# from django.contrib.auth import login
# from django.contrib.auth.decorators import login_required
# from rest_framework import generics, permissions, status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view

# from social_django.utils import load_strategy, load_backend
# from social_core.backends.oauth import BaseOAuth2
# from social_core.exceptions import MissingBackend, AuthTokenError, AuthForbidden
# from rest_framework_jwt.settings import api_settings

# from . import serializers


# jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
# jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


# @login_required
# @api_view(["GET"])
# def home(request):
#     print("hello?")
#     return Response(status=status.HTTP_200_OK)


# class SocialLoginView(generics.GenericAPIView):

#     serializer_class = serializers.SocialSerializer
#     permission_classes = [permissions.AllowAny]

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         provider = serializer.data.get("provider", None)
#         strategy = load_strategy(request)

#         try:
#             backend = load_backend(strategy, name=provider, redirect_uri=None)
#         except MissingBackend:
#             return Response(
#                 {"error": "Please provide a valid provider"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         try:
#             if isinstance(backend, BaseOAuth2):
#                 access_token = serializer.data.get("access_token")
#             user = backend.do_auth(access_token)
#         except HTTPError as error:
#             return Response(
#                 {"error": {"access_token": "Invalid token", "details": str(error)}},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
#         except AuthTokenError as error:
#             return Response(
#                 {"error": "Invalid credentials", "details": str(error)},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         try:
#             authenticated_user = backend.do_auth(access_token, user=user)
#         except HTTPError as error:
#             return Response(
#                 {"error": {"access_token": "Invalid token", "details": str(error)}},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
#         except AuthForbidden as error:
#             return Response(
#                 {"error": "Invalid token", "details": str(error)},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )

#         if authenticated_user and authenticated_user.is_active:
#             login(request, authenticated_user)

#             data = {"token": jwt_encode_handler(jwt_payload_handler(user))}

#             response = {
#                 "email": authenticated_user.email,
#                 "username": authenticated_user.username,
#                 "token": data.get("token"),
#             }

#             return Response(status=status.HTTP_200_OK, data=response)
