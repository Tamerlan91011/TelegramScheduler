# Generated by Django 4.2.1 on 2023-05-07 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0003_user_lesson'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='lesson',
        ),
    ]