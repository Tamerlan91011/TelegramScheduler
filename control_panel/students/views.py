from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Group
from .serializers import GroupSerializer

class GroupID(APIView):
    def get(self, request, group_name):
        group = Group.objects.filter(name=group_name)
        return Response(GroupSerializer(group, many=True).data)