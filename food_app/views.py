from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework import authentication,permissions

from food_app.models import FoodLog
from food_app.serializers import FoodLogSerializer

class FoodLogListCreateView(CreateAPIView,ListAPIView):

    serializer_class=FoodLogSerializer
    queryset=FoodLog.objects.all()
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    # def get(self,request):
    #     instance=FoodLog.objects.all()
    #     serializer_instance=FoodLogSerializer(instance,many=True)
    #     return Response(serializer_instance.data,status=status.HTTP_200_OK)

    # def post(self,request):
    #     form_data=request.data

    #     serializer_instance=FoodLogSerializer(data=form_data)

    #     if serializer_instance.is_valid():
    #         serializer_instance.save()

    #         return Response(serializer_instance.data,status=status.HTTP_201_CREATED)

    #     else:
    #         return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)


class FoodLoogRetriveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    serializer_class=FoodLogSerializer
    queryset=FoodLog.objects.all()
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    # def get(self,request,pk=None):
    #     instance=get_object_or_404(FoodLog,id=pk)
    #     serializer_instance=FoodLogSerializer(instance)
    #     return Response(serializer_instance.data,status=status.HTTP_200_OK)

    # def put (self,request,pk=None):
    #     instance=get_object_or_404(FoodLog,id=pk)
    #     form_data=request.data
    #     serializer_instance=FoodLogSerializer(data=form_data,instance=instance)
    #     if serializer_instance.is_valid():
    #         serializer_instance.save()

    #         return Response(serializer_instance.data,status=status.HTTP_200_OK)

    #     else:
    #         return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

    # def delete(self,request,pk=None):
    #     instance=get_object_or_404(FoodLog,id=pk)
    #     instance.delete()
    #     return Response({"message":"deleted"},status=status.HTTP_200_OK)