from django.conf.urls import url
from fossee4 import views
app_name = "fossee4"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^uploadImage$', views.uploadImage, name='uploadImage'),
    url(r'^getallImages$', views.getallImages, name='getallImages'),
    url(r'^ImagebyId$', views.ImagebyId, name='ImagebyId'),
    url(r'^ImagebyUser$', views.ImagebyUser, name='ImagebyUser'),
    url(r'^doImageUpdate$', views.doImageUpdate, name='doImageUpdate'),
    url(r'^ImageUpdate/(?P<ide>[0-9]+)/', views.ImageUpdate, name='ImageUpdate'),
    url(r'^ImageDelete/(?P<ide>[0-9]+)/', views.ImageDelete, name='ImageDelete'),



]