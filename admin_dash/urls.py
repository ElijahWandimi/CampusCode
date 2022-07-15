from django.urls import path
from . import views

app_name='admin_dash'
urlpatterns = [
    path('', views.index, name='dash')
]