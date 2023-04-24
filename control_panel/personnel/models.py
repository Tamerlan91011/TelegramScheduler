from django.db import models

class User(models.Model):
    name = models.CharField("Имя", max_length=128)
    email = models.EmailField("Почта")