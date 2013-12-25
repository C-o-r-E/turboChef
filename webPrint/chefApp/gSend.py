import sys
import time
from chefApp.models import Printer

cptr = None
elec = None

#############
# Callbacks
#############

def errorcb(data):
	print "error--> " + data

def replycb(data):
	print "reply--> " + data

        if elec == None:
                print "elec is not defined"

	if elec.queueindex > 0: 
                pcnt = (100 * float(elec.queueindex) / len(elec.mainqueue)) 
		print "%f complete" % pcnt

                if cptr != None:
                        cptr.state = "Printing"
                        cptr.percent_complete = pcnt
                        cptr.save()
        else:
                print "q index = %d" % elec.queueindex

def printGcodeFile(path_to_file):
        sys.path.insert(0, '/home/corey/git/Printrun')
        from printrun import gcoder
        from printrun import printcore

        #for testing
        path_to_file = "/home/corey/test1.gcode"

        #default printer
        plist = Printer.objects.all()
        
        if(len(plist) > 0):
                cptr = plist[0]

        try:
                #print "printing gcode for " + path_to_file
                gcFile = open(path_to_file, "rU")

                elec=printcore.printcore('/dev/ttyUSB0', 115200)
                elec.recvcb = replycb
                elec.errorcb = errorcb 
                
                time.sleep(1)
                
                gcode = gcoder.GCode(gcFile)
                
                elec.startprint(gcode)                
                print "done printing?"

        except IOError:
                print "Failed to open gcode file: " + path_to_file
                
