from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
	url("^dec2frac/", views.index, name="dec2frac"),
	url("^result/", views.result, name="result"),
]