from django.conf.urls import url

from web import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^list/(\d+)/', views.list, name='list'),
    url(r'^about/', views.about, name='about'),
    url(r'^info/(\d+)/', views.info, name='info'),
]