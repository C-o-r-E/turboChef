import sys
import time
from chefApp.models import Printer


#TODO: make this a singleton
class gcSender:
        current_printer = None
        device = None

        #############
        # Callbacks
        #############

        def errorcb(self, data):
                print "error--> " + data
                
        def replycb(self, data):
                print "reply--> " + data
                
                if device == None:
                        print "device is not defined"
                        
                if elec.queueindex > 0: 
                        pcnt = (100 * float(elec.queueindex) / len(elec.mainqueue)) 
                        print "%f complete" % pcnt
                                
                        if current_printer != None:
                                current_printer.state = "Printing"
                                current_printer.percent_complete = pcnt
                                current_printer.save()
                else:
                        print "q index = %d" % elec.queueindex

        def printGcodeFile(self, path_to_file):
                sys.path.insert(0, '/home/corey/git/Printrun')
                from printrun import gcoder
                from printrun import printcore

                #for testing
                path_to_file = "/home/corey/test1.gcode"
                
                #default printer
                plist = Printer.objects.all()
                
                if(len(plist) > 0):
                        current_printer = plist[0]
                        
                try:
                        #print "printing gcode for " + path_to_file
                        gcFile = open(path_to_file, "rU")
                        
                        device=printcore.printcore('/dev/ttyUSB0', 115200)
                        device.recvcb = self.replycb
                        device.errorcb = self.errorcb 
                        
                        time.sleep(1)
                        
                        gcode = gcoder.GCode(gcFile)
                        
                        device.startprint(gcode)                
                        print "done printing?"
                        
                except IOError:
                        print "Failed to open gcode file: " + path_to_file
                                
