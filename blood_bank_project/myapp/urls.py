from django.urls import path
from . import views

app_name = 'myapp'
urlpatterns = [

    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('create_account/', views.create_account, name='create_account'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('ajax/load-centers/', views.load_centers, name='ajax_load_centers'),
    path('thanks/', views.thanks, name='thanks'),
]