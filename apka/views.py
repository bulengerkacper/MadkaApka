from django.shortcuts import render, get_object_or_404
from .models import Mother
from .models import Child
import random

def action_list(request):
	mothers = Mother.objects.filter().order_by('secondName')
	return render (request, 'apka/action_list.html', {'mothers':mothers})

def mothers_rank(request):
	mothers = Mother.objects.filter().order_by('points')[:10]
	for mom in mothers:
		mom.getChildrenCount()
		mom.listChildren()
	return render (request, 'apka/mothers_rank.html', {'mothers':mothers})

def mother_detail(request, id):
	mother = get_object_or_404(Mother, id=id)
	return render(request, 'apka/mother_detail.html', {'mother':mother})

def mopsing(request):
	return render(request, 'apka/mopsing.html', {'mopsing':mopsing})

def shopping(request):
	return render(request, 'apka/shopping.html', {'shopping': shopping})

def clubbing(request):
	return render(request, 'apka/clubbing.html', {'clubbing':clubbing})

def tindering(request):
	return render(request, 'apka/tindering.html', {'tindering':tindering})

def perform_action(request,id):
	value = random.randrange(-1000,1000)
	mother = get_object_or_404(Mother, id=11) #dopsiac pobieranie matki z sesji
	print(value)
	if id >= 100 and id < 200:
		if value > 0:
			action="Matka zadowolona. Mopsik dal: " + str(value) + ". Czas na balet!"
		else:
			action="Matka złorzeczy na wszechświat. Mops nic nie dał, musiała wydać " + str(value) + " na bombelka."
	elif id >= 200 and id < 300:
		if value > 0:
			action="Dano mateczce: " + str(value) + " na bułki, wedliny, wódeczkę itd"
		else:
			action="Matka wkurwiona jak Wałęsa na Cenckiewicza. Baba z mopsu powiedziala, ze nic sie jej nie nalezy!"
	elif id >=300 and id < 500:
			if value > 0:
				action="Donosik poszedł pryma sort. Osiągasz spełnienie jako matka. Dostajesz " + str(value) + " punktów."
			else:
				action ="Nie było komu donieść. Nie było kierownika. Smutek zabiera CI " + str(value) + " punktów."
	else:
		action ="ACTION NOT DEFINED YET"
	return render(request, 'apka/action.html', {'action':action})
# Create your views here.
