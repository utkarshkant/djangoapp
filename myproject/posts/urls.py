from django.urls import path
from . import views
from django.http import HttpResponse

urlpatterns = [
    path('', views.posts_list),

]
