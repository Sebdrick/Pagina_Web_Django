from django.contrib import admin
from servicios.models import Servicio

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('Created','Updated')

admin.site.register(Servicio, ServicioAdmin) 