from django.db import models

from students.models import Group

class LessonDate(models.Model):
    date = models.DateField("Дата проведения занятия", auto_now=False, auto_now_add=False, null=True)

class LessonType(models.Model):
    name = models.CharField(max_length=128)

class AcademicCouple(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    
class Lesson(models.Model):
    week = models.IntegerField()
    auditorium = models.CharField(max_length=256, default="Не назначена")
    
    academic_couple = models.ForeignKey(AcademicCouple, null=True, on_delete=models.SET_NULL)
    type_name = models.ForeignKey(LessonType, null=True, on_delete=models.SET_NULL)

    group = models.ManyToManyField(Group)
    lesson_date = models.ManyToManyField(LessonDate)
