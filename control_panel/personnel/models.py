from django.db import models


class User(models.Model):
    name = models.CharField("Имя", max_length=128)
    email = models.EmailField("Почта", null=True)
    telegram_tag = models.CharField("Телеграм", max_length=128, null=True)
    
    def __str__(self) -> str:
        return self.name