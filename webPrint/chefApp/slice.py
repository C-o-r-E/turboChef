from chefApp.models import Printer, Extruder, Material, CADFile
import threading
from time import sleep

#Function for managing slicing
def sliceMan(stlFile):
    #print "sliceMan: %s" % stlFile.name
    stlFile.status_msg = "Uploaded: Waiting for slicing..."
    stlFile.save()
    
    
    stlFile.status_msg = "Done: ready for printing"
    stlFile.save()
