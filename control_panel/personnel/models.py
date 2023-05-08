from django.db import models


class User(models.Model):
    name = models.CharField(max_length=128, verbose_name="Имя")
    email = models.EmailField(null=True, verbose_name="Почта")
    telegram_tag = models.CharField(max_length=128, null=True, verbose_name="Телеграм")
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Преподаватель"
        verbose_name_plural = "Преподаватели"