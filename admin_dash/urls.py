from django.urls import path
from . import views

app_name='admin_dash'
urlpatterns = [
    path('', views.index, name='dash'),
    path('login/', views.login, name='lec_login'),
    path('signup/', views.signup, name='lec_signup')
]