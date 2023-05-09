from django.urls import path
from . import views
  
urlpatterns = [
    path('group-name/<str:group_name>/', views.GroupByName.as_view()),
    path('group-id/<int:group_id>/', views.GroupById.as_view()),
    path('telegram/<int:tg_chat_id>/', views.StudentTelegramChatId.as_view())
]