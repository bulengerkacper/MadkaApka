from django.shortcuts import render
from .models import Mother
def mothers_list(request):
	mothers = Mother.objects.filter().order_by('secondName')
	return render (request, 'apka/mothers_list.html', {'mothers':mothers})
# Create your views here.
