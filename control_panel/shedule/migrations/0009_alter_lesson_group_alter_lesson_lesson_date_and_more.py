# Generated by Django 4.2.1 on 2023-05-08 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personnel', '0004_remove_user_lesson'),
        ('students', '0004_rename_chat_id_user_telegram_chat_number'),
        ('shedule', '0008_lesson_teacher_alter_lesson_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='group',
            field=models.ManyToManyField(db_index=True, to='students.group'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_date',
            field=models.ManyToManyField(db_index=True, to='shedule.lessondate'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='teacher',
            field=models.ManyToManyField(db_index=True, to='personnel.user'),
        ),
    ]
