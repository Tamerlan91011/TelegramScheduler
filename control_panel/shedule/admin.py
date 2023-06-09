from django.contrib import admin
from .models import Lesson, LessonDate, LessonType, AcademicCouple

# Register your models here.

class LessonDateAdmin(admin.ModelAdmin):
    list_display = ["date"]


class  LessonTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]


class AcademicCoupleAdmin(admin.ModelAdmin):
    list_display = ["start_time", "end_time"]


class LessonAdmin(admin.ModelAdmin):
    list_filter = ['week']
    list_select_related = ["academic_couple", "type_name"]
    list_display = ["week", "academic_couple", "type_name", "auditorium", "display_teacher", "display_group", "display_date"]
    radio_fields = {"week": admin.HORIZONTAL, "type_name": admin.HORIZONTAL}


admin.site.register(LessonDate, LessonDateAdmin)
admin.site.register(LessonType, LessonTypeAdmin)
admin.site.register(AcademicCouple, AcademicCoupleAdmin)
admin.site.register(Lesson, LessonAdmin)
