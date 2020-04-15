from django.urls import path
from django.conf.urls import url
from django.conf.urls import include

from . import views
#from django.urls import include
app_name='companysapp'
urlpatterns = [
    path('', views.index, name='index'),
     url('callback/', include('companysapp.urls')),
     path('',views.callback,name='callback'),
]
