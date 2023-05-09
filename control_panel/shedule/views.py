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
    
class WeekLessons(APIView):    
    def get(self, request, week_id):
        lesson = Lesson.objects.filter(week=week_id)
        
        serialized_lessons = LessonSerializer(lesson, many=True)
        return Response(serialized_lessons.data)

class FirstLesson(APIView):
    def get(self):
        first_lesson = Lesson.objects.first()
        
        serialized__first_lesson = LessonSerializer(first_lesson)
        return Response(serialized__first_lesson.data)

class GroupLessonsDate(APIView):
    def get(self, request, group_id, date_id):
        
        lesson = Lesson.objects.filter(group=group_id, lesson_date=date_id)
        
        serialized_lessons = LessonSerializer(lesson, many=True)
        return Response(serialized_lessons.data)

class GroupLessonsWeek(APIView):
    def get(self, request, group_id, week_id):
        
        lesson = Lesson.objects.filter(group=group_id, week=week_id)
        
        serialized_lessons = LessonSerializer(lesson, many=True)
        return Response(serialized_lessons.data)