from django.contrib import admin
from general.models import *
# Register your models here.

class DirectorAdmin(admin.ModelAdmin):
    pass



admin.site.register(Cohorte)
admin.site.register(Inscripcion)
admin.site.register(carta_referencia)
admin.site.register(Aspirante)
admin.site.register(Director, DirectorAdmin)
admin.site.register(DirectorXMaestria)
admin.site.register(Maestria)
admin.site.register(compromisos)