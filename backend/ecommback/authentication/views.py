from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from authentication.serializers import *


class UserRegistrationAPIView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            response = {"message": "verification mail sended"}
            return Response(response, status=status.HTTP_200_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
