"""misitio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from misitio.views import raiz, hola, fecha_actual, horas_delante, vista_actual_url, mostrar_navegador, atributos_meta
from django.contrib import admin

from biblioteca import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', raiz),
    url(r'^hola/$', hola),
    url(r'^fecha/$', fecha_actual),
    url(r'^fecha/mas/(\d{1,2})/$', horas_delante),
    url(r'^url/$', vista_actual_url),
    url(r'^navegador/$', mostrar_navegador),
    url(r'^atributos/$', atributos_meta),

    # Url aplicacion biblioteca
    url(r'^formulario-buscar/$', views.formulario_buscar),
    url(r'^buscar/$', views.buscar)
]
