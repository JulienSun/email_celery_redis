from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from email_app.tasks import send_email
from datetime import datetime


class SendEmailView(APIView):
    def get(self, request):
        task_id = send_email.delay("116245496@qq.com")
        print("send email to celery: " + str(task_id))
        return Response(status=status.HTTP_200_OK)
