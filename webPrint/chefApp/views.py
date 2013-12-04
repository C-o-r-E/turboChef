from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic

from chefApp.models import Printer, Extruder, Material

class IndexView(generic.ListView):
    template_name = 'chefApp/index.html'
    context_object_name = 'printer_list'

    def get_queryset(self):
        return Printer.objects.all()

def printerDetails(request, printer_id):
    detail_printer = get_object_or_404(Printer, pk=printer_id)
    #detail_printer = Printers.objects.get(pk=printer_id)
    related_extruder_list = Extruder.objects.filter(printer=detail_printer.id)
    detail_list = []

    #for e in related_extruder_list:
        #detail_list.append( (e, e.material )

    return render(request, 'chefApp/printer_details.html', {
            'printer' : detail_printer,
            'extruders' : related_extruder_list,
            })
