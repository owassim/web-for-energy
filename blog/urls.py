from django.conf.urls import url
from . import views

urlpatterns = [
    path('accueil', views.home),
    path('base', views.acc),
    path('date', views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>/',views.addition),
    url(r'^$', views.post_list, name='post_list'),
    
    ]