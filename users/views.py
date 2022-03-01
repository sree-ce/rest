from datetime import datetime
from http.client import IM_USED
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UseSerializer
from .models import UserDetails
from rest_framework.exceptions import AuthenticationFailed
import jwt , datetime
# Create your views here.

#------Register View-------->
class register(APIView):
    def post(self,request):
        serializer = UseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

#------Login View---------->
class LoginView(APIView):
    def post(self,request):
        username = request.data['username']
        password = request.data['password']

        user = UserDetails.objects.filter(username = username,password=password).first()

        if user is None:
            raise AuthenticationFailed('user not found')
      

        return Response({ 
            "message":"success"
        })
