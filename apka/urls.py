from django.urls import path
from . import views

urlpatterns = [
		path('', views.mothers_list, name='mothers_list'),
]