"""
URL configuration for store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path
from main.views import index, catalog, signup
from item.views import item
from cart.views import add_to_cart, cart, checkout

urlpatterns = [
    path('', index, name='index'),
    path('<slug:slug>', item, name='item'),
    path('catalog/', catalog, name='catalog'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('cart/', cart, name='cart'),
    path('cart/checkout', checkout, name='checkout'),
    path('add_to_cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
