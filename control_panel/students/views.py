from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Group, User
from .serializers import GroupSerializer, UserSerializer

class GroupByName(APIView):
    def get(self, request, group_name):
        group = Group.objects.get(name=group_name)
        return Response(GroupSerializer(group).data)

class GroupById(APIView):
    def get(self, request, group_id):
        group = Group.objects.get(id=group_id)
        return Response(GroupSerializer(group).data)
    
class StudentTelegramChatId(APIView):
    def get(self, request, tg_chat_id):
        student = User.objects.get(telegram_chat_number=tg_chat_id)
        return Response(UserSerializer(student).data)