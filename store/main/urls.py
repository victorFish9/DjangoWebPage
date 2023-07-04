from django.urls import path
from main.views import index, catalog, signup, myaccount, edit_myaccount
from django.contrib.auth import views
from item.views import item

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('myaccount/', myaccount, name='myaccount'),
    path('edit_myaccount/', edit_myaccount, name='edit_myaccount'),
    path('<slug:slug>', item, name='item'),
    path('catalog/', catalog, name='catalog'),
]