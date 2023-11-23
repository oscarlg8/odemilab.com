from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Factor, SubFactor
from django.shortcuts import get_object_or_404

# Create your views here.
def about(request):
    return render(request, 'lindex.html')

def docurey(request, id):
    subfactor = get_object_or_404(SubFactor, id=id)
    return HttpResponse('el subfactor que buscas es %s'% subfactor.name)

def podcast(request):
    return HttpResponse("Como te ganas la vida?")

def reynogpt(request):
    return HttpResponse("Reynogpt")