from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
url(r'^surveys/new/$', views.new),
url(r'^surveys/$', views.create),  
 # This line has changed!
]