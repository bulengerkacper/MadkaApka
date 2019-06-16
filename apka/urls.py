from django.urls import path
from . import views

urlpatterns = [
		path('', views.action_list, name='action_list'),
		path('mothersrank', views.mothers_rank, name='mothers_rank'),
		path('mother/<int:id>', views.mother_detail, name='mother_detail'),
]
