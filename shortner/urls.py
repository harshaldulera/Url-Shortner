from django.urls import path
from . import views
from shortner.views import go

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('<str:pk>', go, name='redirect')
]