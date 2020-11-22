from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import  User
# urlpatterns = [
#     path('', views.home, name='home'),
#     # path('print', views.print, name='print'),
# ]
urlpatterns = [
    path('a', views.start , name='start') ,
    path('', views.top_country , name='top_country') ,
    path('details', views.home , name='home') ,
  
]