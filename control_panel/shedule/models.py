from django.db import models

from students.models import Group
from personnel.models import User as Teacher

class LessonDate(models.Model):
    date = models.DateField("Дата проведения занятия", auto_now=False, auto_now_add=False, null=True)
    
    def __str__(self) -> str:
        return str(self.date)


class LessonType(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self) -> str:
        return self.name

class AcademicCouple(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    def __str__(self) -> str:
        return f'{self.start_time} - {self.end_time}'


class Lesson(models.Model):
    WEEK_CHOICES = (
        (1, "Первая"),
        (2, "Вторая")
    )
    week = models.PositiveSmallIntegerField(default=int(1), choices=WEEK_CHOICES)
    auditorium = models.CharField(max_length=256, default="Не назначена")
    
    academic_couple = models.ForeignKey(AcademicCouple, null=True, on_delete=models.SET_NULL)
    type_name = models.ForeignKey(LessonType, null=True, on_delete=models.SET_NULL)

    group = models.ManyToManyField(Group)
    lesson_date = models.ManyToManyField(LessonDate)
    
    teacher =  models.ManyToManyField(Teacher)
