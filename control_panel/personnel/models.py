from django.db import models

from shedule.models import Lesson

class User(models.Model):
    name = models.CharField("Имя", max_length=128)
    email = models.EmailField("Почта", null=True)
    telegram_tag = models.CharField("Телеграм", max_length=128, null=True)
    
    lesson =  models.ManyToManyField(Lesson)