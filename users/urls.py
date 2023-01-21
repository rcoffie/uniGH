from django.urls import path
from users import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('signup/', views.signup,name='signup'),
    path('login_request/',views.login_request,name='login_request')
]
