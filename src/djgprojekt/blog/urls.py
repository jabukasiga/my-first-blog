from django.urls import path
from . import views

urlpatterns = [
	path('blabla', views.post_list, name='post_list'),
	path('', views.strona2, name='strona2'),
	path('szansa/', views.last_chance, name='chance')

]