from django.urls import path
from basic_app import views

app_name = 'basic_app'


urlpatterns = [
    path('',views.login_index,name='login_index'),
    path('register/',views.register, name='register'),
    path('user_login/',views.user_login,name='user_login'),

]
