from chefApp.models import Printer, Extruder, Material, CADFile
import threading
from time import sleep
from django.conf import settings
import subprocess

sliceFail = False

#Function for managing slicing
def sliceMan(stlFile):
    #print "sliceMan: %s" % stlFile.name
    stlFile.status_msg = "Uploaded: Waiting for slicing..."
    stlFile.full_path = stlFile.cadfile.path
    stlFile.path_to_gcode = settings.GCODE_PATH + stlFile.name + '.gcode'
    stlFile.save()
    

    #now we actually invoke slic3r
    try:
        subprocess.check_output(
            ['perl', settings.SLIC3R_PATH, stlFile.cadfile.path, '-o', stlFile.path_to_gcode]
        )
    except subprocess.CalledProcessError:
        print "Error slicing " + stlFile.name
        sliceFail = True
        stlFile.status_msg = "Error: Slicing failed"
    
    if sliceFail == False:
        stlFile.status_msg = "Done: ready for printing"
    stlFile.save()
