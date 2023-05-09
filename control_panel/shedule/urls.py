from django.urls import path
from . import views
  
urlpatterns = [
    path('lessons/', views.AllLessons.as_view()),
    path('lessons/group/<int:group_id>/week/<int:week_id>', views.GroupLessonsWeek.as_view()),
    path('lessons/group/<int:group_id>/date/<int:date_id>', views.GroupLessonsDate.as_view()),
    path('lesson-date/<str:str_date>/', views.DateID.as_view())
]