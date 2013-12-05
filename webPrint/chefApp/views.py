from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, render_to_response
from django.views import generic
from django.template import RequestContext
from django.utils import timezone
from django.core.urlresolvers import reverse

from chefApp.models import Printer, Extruder, Material, CADFile
from chefApp.forms import CADForm

class IndexView(generic.ListView):
    template_name = 'chefApp/index.html'
    context_object_name = 'printer_list'

    def get_queryset(self):
        return Printer.objects.all()

class FileListView(generic.ListView):
    template_name = 'chefApp/file_list.html'
    context_object_name = 'file_list'

    def get_queryset(self):
        return CADFile.objects.all()

FileListView.plain_view = staticmethod(FileListView.as_view())

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


def upload(request):
    if request.method == 'POST':
        form = CADForm(request.POST, request.FILES)
        if form.is_valid():
            newCAD = CADFile(
                cadfile = request.FILES['cadfile'],
                name = request.FILES['cadfile'].name,
                file_size = request.FILES['cadfile'].size,
                upload_time = timezone.now()
                )
            newCAD.save()

        return HttpResponseRedirect(reverse(FileListView.plain_view))

    else:
        form = CADForm()

    return render_to_response(
        'chefApp/file_upload.html',
        {'form': form},
        context_instance = RequestContext(request)
        )
            
