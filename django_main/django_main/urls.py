"""
URL configuration for django_main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_smartwork_app.urls') ),
    path('register_api/', include('my_smartwork_app.urls')),
    path('login/', include('my_smartwork_app.urls')),
    path('api/CheckIn/',  include('my_smartwork_app.urls')),
    path('api/User_info', include('my_smartwork_app.urls')),
    path('CheckIn_info_api/', include('my_smartwork_app.urls')),
    path('api/Assignment/',include('my_smartwork_app.urls') ),
    path('Order_api/', include('my_smartwork_app.urls')),
    path('Post_order_api/',include('my_smartwork_app.urls') ),
    path('Approved_order_api/', include('my_smartwork_app.urls')),
    path('Decline_order_api/',include('my_smartwork_app.urls' ))
]
