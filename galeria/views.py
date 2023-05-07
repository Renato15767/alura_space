"""" views.py cuida do que vai ser exibido em cada página e 
     qual conteúdo vão ter """

from django.shortcuts import render

# Create your views here.
# Será criado uma def quando tiver um novo arq. html

def index(request):
    return render(request, 'galeria/index.html')

def imagem(request):
    return render(request, 'galeria/imagem.html')

