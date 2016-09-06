from django.conf.urls import url

from . import views

app_name = "movies"

urlpatterns = [
	# /
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /list
    url(r'^list/$', views.ListView.as_view(), name='list'),

    # /424/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]