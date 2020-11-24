from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name ='home'),
    path('course/<int:course_id>',views.course_detail, name='course_detail'),
    path('register', views.register, name='register'),
    path('logout', views.logout_request, name='logout'),
    path('login', views.login_request, name='login'),
    ]