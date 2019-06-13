from django.shortcuts import render, get_object_or_404
from .models import Mother
from .models import Child

def mothers_list(request):
	mothers = Mother.objects.filter().order_by('secondName')
	return render (request, 'apka/mothers_list.html', {'mothers':mothers})

def mothers_rank(request):
	mothers = Mother.objects.filter().order_by('points')[:10]
	for mom in mothers:
		a=mom.getChildrenCount()
		print(a)
		mom.listChildren()
	return render (request, 'apka/mothers_rank.html', {'mothers':mothers})

def mother_detail(request, id):
	mother = get_object_or_404(Mother, id=id)
	return render(request, 'apka/mother_detail.html', {'mother':mother})
# Create your views here.
