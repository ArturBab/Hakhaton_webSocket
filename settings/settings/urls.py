
from django.contrib import admin
from django.urls import path
from myproj import views
from django.urls import re_path
from myproj import consumers

websocket_urlpatterns = [
    re_path(r'ws/socket-server/', consumers.TestConsumer.as_asgi())
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.lobby),
    path('', views.get_data),
]
