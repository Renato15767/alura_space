"""" 
- urls.py cuida das rotas das aplicações

"""

from django.contrib import admin
from django.urls import path, include

# O include é responsável por pegar o arq. 'urls.py' de 'galeria',
# assim isolando a url 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),
]
