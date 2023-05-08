from django.db import models

class Group(models.Model):
    name = models.CharField("Наименование", max_length=256)
    
    def __str__(self) -> str:
        return self.name

class User(models.Model):
    name = models.CharField("ФИО", max_length=256)
    student_card_number = models.IntegerField("Номер студенческого билета")
    password = models.CharField("Пароль", max_length=256)
    telegram_chat_number = models.IntegerField("Номер чата в телеграм", null=True)
    
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL)