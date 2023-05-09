from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=256, verbose_name="Наименование")
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"

class User(models.Model):
    name = models.CharField(max_length=256, verbose_name="ФИО")
    student_card_number = models.IntegerField(verbose_name="Номер студенческого билета")
    password = models.CharField(max_length=256, verbose_name="Пароль")
    telegram_chat_number = models.IntegerField(null=True, verbose_name="Номер чата в телеграм")
    
    group = models.ForeignKey(Group, null=True, on_delete=models.SET_NULL, verbose_name="Группа")

    def __str__(self) -> str:
        return f"{self.name}, {self.student_card_number}"

    class Meta: 
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"