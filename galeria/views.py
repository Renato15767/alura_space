"""" views.py cuida do que vai ser exibido em cada página e 
     qual conteúdo vão ter """

from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'galeria/index.html')

