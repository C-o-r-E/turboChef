from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, render_to_response
from django.views import generic
from django.template import RequestContext
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.core import serializers

from django.views.decorators.csrf import csrf_exempt

from chefApp.models import Printer, Extruder, Material, CADFile
from chefApp.forms import CADForm

from chefApp.slice import sliceMan
from chefApp.gSend import gcSender

from threading import Thread

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

def api_printer_list(request):
    api_data = serializers.serialize("json", Printer.objects.all())
    return HttpResponse(api_data, content_type="application/json")
    

def api_file_list(request):
    api_data = serializers.serialize("json", CADFile.objects.all(), fields=('name', 'file_size', 'status_msg'))
    return HttpResponse(api_data, content_type="application/json")

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

#this should be done with a post
def doPrint(request, file_id):
    file2print = get_object_or_404(CADFile, pk=file_id)

    gcs = gcSender()
    printThread = Thread(target=gcs.printGcodeFile, args=(file2print.path_to_gcode,))
    printThread.start()
    
    return render(request, 'chefApp/print.html', { 'file' : file2print, })

@csrf_exempt
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

            newThread = Thread(target=sliceMan, args=(newCAD,)) #need to make sure this wont get GCd
            newThread.start()

        return HttpResponseRedirect(reverse(FileListView.plain_view))

    else:
        form = CADForm()

    return render_to_response(
        'chefApp/file_upload.html',
        {'form': form},
        context_instance = RequestContext(request)
        )

