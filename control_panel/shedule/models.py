from django.db import models

from students.models import Group
from personnel.models import User as Teacher

class LessonDate(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False, null=True, verbose_name="Дата проведения занятия")
    
    def __str__(self) -> str:
        return str(self.date)
    
    class Meta:
        verbose_name ="Дата занятия"
        verbose_name_plural = "Даты занятий"


class LessonType(models.Model):
    name = models.CharField(max_length=128, verbose_name="Название")
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Тип занятия"
        verbose_name_plural = "Тип занятий"

class AcademicCouple(models.Model):
    start_time = models.TimeField(verbose_name="Время начала")
    end_time = models.TimeField(verbose_name="Время окончания")
    
    def __str__(self) -> str:
        return f'{self.start_time} - {self.end_time}'
    
    class Meta:
        verbose_name = "Время занятия"
        verbose_name_plural = "Время занятий"


class Lesson(models.Model):
    WEEK_CHOICES = (
        (1, "Первая"),
        (2, "Вторая")
    )
    week = models.PositiveSmallIntegerField(default=int(1), choices=WEEK_CHOICES, verbose_name="Учебная неделя")
    auditorium = models.CharField(max_length=256, default="Не назначена", verbose_name="Аудитория")
    
    academic_couple = models.ForeignKey(AcademicCouple, null=True, on_delete=models.SET_NULL, verbose_name="Время занятий")
    type_name = models.ForeignKey(LessonType, null=True, on_delete=models.SET_NULL, verbose_name="Тип занятия")

    group = models.ManyToManyField(Group, verbose_name="Группа")
    lesson_date = models.ManyToManyField(LessonDate, verbose_name="Дата занятия")
    
    teacher =  models.ManyToManyField(Teacher, verbose_name="Преподаватель", db_index=True)

    class Meta:
        verbose_name = "Занятие"
        verbose_name_plural = "Занятия"

    def display_group(self):
        return ', '.join(group.name for group in self.group.all()[:3])
    
    def display_date(self):
        return ', '.join(str(lesson_date.date) for lesson_date in self.lesson_date.all()[:3])

    display_group.short_description = 'Учебные группы'
    display_date.short_description = 'Даты проведения занятий'