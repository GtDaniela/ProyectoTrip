from django.contrib import admin
#from .models import Viajero,Publicacion,Video,Foto,Comentario,Like,Seguido,Seguidor,Alojamiento,
from .models import *
# Register your models here.
admin.site.register(Viajero)
admin.site.register(Publicacion)
admin.site.register(Video)
admin.site.register(Foto)
admin.site.register(Comentario)
admin.site.register(Like)
admin.site.register(Seguidor)
admin.site.register(Alojamiento)
admin.site.register(Alojamiento_prestado)
admin.site.register(Prestar_alojamiento)