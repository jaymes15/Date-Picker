from . import views
from django.conf.urls import url
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

 
app_name= 'datepickerapp'
urlpatterns = [
	path('', views.homepage,name='homepage'),
	
	]