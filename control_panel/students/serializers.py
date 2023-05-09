from rest_framework import serializers

from .models import Group, User

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']
         
class UserSerializer(serializers.ModelSerializer):
    group = GroupSerializer()
    
    class Meta:
        model = User
        fields = ['id', 'student_card_number', 'telegram_chat_number', 'name', 'group']