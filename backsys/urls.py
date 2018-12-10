from django.conf.urls import url

from backsys import views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^index/', views.index, name='index'),
    url(r'^article/', views.article, name='article'),

    url(r'^add_article/', views.add_article, name='add_article'),
    url(r'^del_art/(\d+)/', views.del_art, name='del_art'),
    url(r'^edit_art/(\d+)/', views.edit_art, name='edit_art'),
]