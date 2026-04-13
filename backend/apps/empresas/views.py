#Criando uma view para listar as empresas   

from django.http import JsonResponse
from .models import Empresa

def listar_empresas(request):
    empresas = Empresa.objects.all().values()
    return JsonResponse(list(empresas), safe=False)