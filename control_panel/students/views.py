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
        try:
            student = User.objects.get(telegram_chat_number=tg_chat_id)
        except:
            return Response(status=400)
        return Response(UserSerializer(student).data)
    
    
# class StudentChatId(APIView):
#     def put(self, request, *args, **kwargs):
#         student_card_number = kwargs.get('student_card_number', None)
        
#         if not student_card_number:
#             return Response({'error': 'Method PUT not allowed'})
        
#         try:
#             instance = User.objects.get(student_card_number=student_card_number)
#         except:
#             return Response({'error': 'Object does not exists'})
        
#         serializer = UserSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
        
#         return Response({'post': serializer.data})