from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path("" , home , name="home"),
    path("car/" , car , name="car"),
    path("error/" , error , name="error404"),
]
urlpatterns+=static(settings.STATIC_URL,documnet_root = settings.STATIC_ROOT)