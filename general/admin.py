from django.contrib import admin

from general.models import Cohorte, Inscripcion, carta_referencia

# Register your models here.
admin.site.register(Cohorte)
admin.site.register(Inscripcion)
admin.site.register(carta_referencia)