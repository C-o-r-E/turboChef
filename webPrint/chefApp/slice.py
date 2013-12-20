from chefApp.models import Printer, Extruder, Material, CADFile
import threading

class sliceThread(threading.Thread):
    def run(self, stlFile):
        print "%s: started thread with %s" % (self.getName(), stlFile.name) 

        print "%s: done" % (self.getName())
