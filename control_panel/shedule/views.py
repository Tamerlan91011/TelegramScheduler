from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Lesson
from .serializers import *
        
class AllLessons(APIView):
    def get(self, request):
        all_lessons = Lesson.objects.all()
        serialized_lessons = LessonSerializer(all_lessons, many=True)
        return Response(serialized_lessons.data)
    
class SingleLesson(APIView):    
    def get(self, request, pk):
        lesson = Lesson.objects.get(id=pk)
        serialized_lessons = LessonSerializer(lesson)
        return Response(serialized_lessons.data)

class FirstLesson(APIView):
    def get(self):
        first_lesson = Lesson.objects.first()
        serialized__first_lesson = LessonSerializer(first_lesson)
        return Response(serialized__first_lesson.data)