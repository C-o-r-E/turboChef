from django.contrib import admin
from chefApp.models import Printer, Material, Extruder, CADFile


admin.site.register(Printer)
admin.site.register(Material)
admin.site.register(Extruder)
admin.site.register(CADFile)
