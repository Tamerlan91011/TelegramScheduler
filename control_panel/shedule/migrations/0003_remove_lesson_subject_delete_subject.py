# Generated by Django 4.1.7 on 2023-04-24 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shedule', '0002_alter_lesson_academic_couple_alter_lesson_group_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='subject',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
