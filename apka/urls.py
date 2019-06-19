from django.urls import path
from . import views

urlpatterns = [
		path('', views.action_list, name='action_list'),
		path('mothersrank', views.mothers_rank, name='mothers_rank'),
		path('mother/<int:id>', views.mother_detail, name='mother_detail'),
		path('mopsing', views.mopsing, name='mopsing'),
		path('shopping', views.shopping, name='shopping'),
		path('clubbing', views.clubbing, name='clubbing'),
		path('tindering', views.tindering, name='tindering'),
		path('action/<int:id>', views.perform_action, name='perform_action')
]
