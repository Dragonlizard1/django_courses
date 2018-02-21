from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
url(r'^$', views.index),
url(r'^new$', views.new),
url(r'^reset$', views.reset)

 # This line has changed!
]