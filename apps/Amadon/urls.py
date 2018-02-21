from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
url(r'^$', views.start),
url(r'^amadon/$', views.index),
url(r'^process$', views.process),
url(r'^amadon/checkout/$', views.result)

 # This line has changed!
]