
from django.contrib import admin
from django.urls import path, re_path
from myproj import views
from myproj import consumers

websocket_urlpatterns = [
    re_path(r'ws/socket-server/', consumers.TestConsumer.as_asgi())
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.get_data),
    path('test/', views.index),
]
