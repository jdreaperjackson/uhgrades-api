from django.urls import path
from .views import grade_list, grade_info

urlpatterns = [
    path('api/', grade_list),
    path('info/<int:pk>/', grade_info)
]
