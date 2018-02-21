from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
url(r'^register/$', views.create),
url(r'^login/$', views.login),
url(r'^users/new/$', views.new),
url(r'^users/$', views.display), # This line has changed!
]