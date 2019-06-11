from django.shortcuts import render
from .models import Mother

def mothers_list(request):
	mothers = Mother.objects.filter().order_by('secondName')
	return render (request, 'apka/mothers_list.html', {'mothers':mothers})

def mothers_rank(request):
	mothers = Mother.objects.filter().order_by('points')[:10]
	return render (request, 'apka/mothers_rank.html', {'mothers':mothers})

# Create your views here.
