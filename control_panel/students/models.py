from django.db import models

class Group(models.Model):
    name = models.CharField("Наименование", max_length=256)

class User(models.Model):
    name = models.CharField("ФИО", max_length=256)
    student_card_id = models.IntegerField("Номер студенческого билета")
    password = models.CharField("Пароль", max_length=256)
    chat_id = models.IntegerField("Номер чата в телеграм", null=True)
    
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)