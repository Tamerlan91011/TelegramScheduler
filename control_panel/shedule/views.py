from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Lesson, LessonDate
from .serializers import *
        
class AllLessons(APIView):
    def get(self, request):
        all_lessons = Lesson.objects.all()
        return Response(LessonSerializer(all_lessons, many=True).data)
    
class WeekLessons(APIView):    
    def get(self, request, week_id):
        lesson = Lesson.objects.filter(week=week_id)
        return Response(LessonSerializer(lesson, many=True).data)

class FirstLesson(APIView):
    def get(self):
        first_lesson = Lesson.objects.first()
        return Response(LessonSerializer(first_lesson).data)

class GroupLessonsDate(APIView):
    def get(self, request, group_id, date_id):
        lesson = Lesson.objects.filter(group=group_id, lesson_date=date_id)
        return Response(LessonSerializer(lesson, many=True).data)

class GroupLessonsWeek(APIView):
    def get(self, request, group_id, week_id):
        lesson = Lesson.objects.filter(group=group_id, week=week_id)
        return Response(LessonSerializer(lesson, many=True).data)

class LessonDateByDate(APIView):
    def get(self, request, str_date):
        lesson_date = LessonDate.objects.get(date=str_date)
        return Response(LessonDateSerializer(lesson_date).data)