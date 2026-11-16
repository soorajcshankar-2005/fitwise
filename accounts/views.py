from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
from accounts.serializers import UserSerializer


class UserCreateView(APIView):
    def post(self,request):
        form_data=request.data
        serializer_insatance=UserSerializer(data=form_data)
        if serializer_insatance.is_valid():
            cleaned_data=serializer_insatance.validated_data
            instance=User.objects.create_user(**cleaned_data)
            serializer_insatance=UserSerializer(instance)
            return Response(serializer_insatance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_insatance.errors,status=status.HTTP_400_BAD_REQUEST)