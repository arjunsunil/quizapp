
from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', views.home, name='home'),
   url(r'^results/', views.results, name='results'),
   url(r'^other_results/', views.other_results, name='other_results'),
]
