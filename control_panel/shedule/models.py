from django.db import models

from students.models import Group

class Subject(models.Model):
    name = models.CharField(max_length=256)
    
class AcademicCouple(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    
class Lesson(models.Model):
    week = models.IntegerField()
    weekday = models.IntegerField()
    
    academic_couple = models.ForeignKey(AcademicCouple, null=True, on_delete=models.SET_NULL)
    
    subject = models.ManyToManyField(Subject)
    group = models.ManyToManyField(Group)
