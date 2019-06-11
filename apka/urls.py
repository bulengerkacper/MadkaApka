from django.urls import path
from . import views

urlpatterns = [
		path('', views.mothers_list, name='mothers_list'),
		path('mothersrank', views.mothers_rank, name='mothers_rank')
]