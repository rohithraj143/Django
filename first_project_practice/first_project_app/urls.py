from django.conf.urls import url
from first_project_app import views

urlpatterns = [
    url(r'^model', views.modelTest, name='modelTest'),
    url(r'^index', views.index, name='indexing'),
    url(r'^help', views.help, name='help'),
    url(r'^users', views.users, name='listOfUsers'),
]
