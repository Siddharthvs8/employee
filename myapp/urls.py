from django.urls import path, include
from .import views

urlpatterns = [
    path('welcome/', views.welcome),
    path('add/', views.add),
    path('add_all/', views.add_all),
    path('update/<int:sid>',views.update),
    path('delete/<int:sid>',views.delete),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),



]
