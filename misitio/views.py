from django.template import Template, Context
from django.http import Http404, HttpResponse
import datetime
from django.template.loader import get_template

#Importando shortcuts (Atajo para no utilizar get_template)
from django.shortcuts import render

def hola(request):
  return HttpResponse('Hola Mundo')


def raiz(request):
  return HttpResponse('Raiz del sitio')


def fecha_actual(request):
  ahora = datetime.datetime.now()
  return render(request, 'fecha_actual.html', {'fecha_actual': ahora,})


def horas_delante(request, offset):
  try:
    offset = int(offset)
  except ValueError:
    raise Http404()
  dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
  return render(request, 'fecha_adelante.html', {'hora_siguiente': dt, 'horas': offset})


def vista_actual_url(request):
  return HttpResponse("bienvenido a mi pagina en %s" % request.path)

def mostrar_navegador(request):
  ua = request.META.get('HTTP_USER_AGENT', 'Unknown')
  return HttpResponse("Tu navegador es: %s" % ua)

def atributos_meta(request):
  valor = request.META.items()
  html = []
  for k, v in valor:
    html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
  return HttpResponse('<table>%s</table>' % '\n'.join(html))


# Version: obteniendo archivo del disco
# def fecha_actual(request):
#   ahora = datetime.datetime.now()
#   fp = open('/home/danny/Documentos/django/misitio/miplantilla.html')
#   t = Template(fp.read())
#   fp.close()
#   html = t.render(Context({'fecha_actual': ahora}))
#   return HttpResponse(html)

# Utilizando plantillas manualmente y crear los objetos Context y HttpResponse manualmente
# def fecha_actual(request):
#   ahora = datetime.datetime.now()
#   t = get_template('miplantilla.html')
#   html = t.render({'fecha_actual': ahora})
#   return HttpResponse(html)

# horas_delanto manualmente
# def horas_delante(request, offset):
#   try:
#     offset = int(offset)
#   except ValueError:
#     raise Http404()
#   dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
#   html = "<html><body><h1>En %s hora(s), seran:</h1> <h3>%s</h3></body></html>" % (offset, dt)
#   return HttpResponse(html)