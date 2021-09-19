from django.urls import path

from . import views
from .views import grade_list, grade_info, GradeListfilter
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="home"),
    path('api/', grade_list),
    path('info/<int:pk>/', grade_info),
    path('search/', GradeListfilter.as_view(), name='postsearch')
]
