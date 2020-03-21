from django.contrib import admin
from biblioteca.models import Editor, Autor, Libro

class AutorAdmin(admin.ModelAdmin):
  list_display = ('nombre', 'apellidos', 'email')
  search_fields =('nombre', 'apellidos')


class LibroAdmin(admin.ModelAdmin):
  list_display = ('titulo', 'editor', 'fecha_publicacion')  # Campos de la lista de cambios
  list_filter = ('fecha_publicacion',)  #  Agregar filtro de fecha
  date_hierarchy = 'fecha_publicacion'  # Jerarquia de fecha
  ordering = ('-fecha_publicacion',)  # Agregando Ordenamiento por fecha
  # fields = ('titulo', 'autores', 'editor', 'portada')  # Modificando campos del formulario de edicion
  filter_horizontal = ('autores',)  # Agregar filtro para campos ManyToManyField, tambien valido para campos multiples, filter_vertical es lo mismo solo que diferente dispoicion
  raw_id_fields = ('editor',)  # Para foreingkey, busca al editor en una nueva interfaz


admin.site.register(Editor)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)

