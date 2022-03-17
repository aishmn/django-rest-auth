from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class LoginAPIView(APIView):
    def post(self, request):
        return Response({"message": "success"})


class RegisterAPIView(APIView):
    def post(self, request):
        return Response({"message": "success"})
