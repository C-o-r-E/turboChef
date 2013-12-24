import sys
import time





#############
# Callbacks
#############

def errorcb(data):
	print "error--> " + data

def replycb(data):
	print "reply--> " + data

	if p.queueindex > 0: 
		print "%f complete" % (100 * float(p.queueindex) / len(p.mainqueue)) 


def printGcodeFile(path_to_file):
        sys.path.insert(0, '/home/corey/git/Printrun')
        from printrun import gcoder
        from printrun import printcore

        #for testing
        path_to_file = "/home/corey/test1.gcode"

        try:
                #print "printing gcode for " + path_to_file
                gcFile = open(path_to_file, "rU")

                p=printcore.printcore('/dev/ttyUSB0', 115200)
                p.recvcb = replycb
                p.errorcb = errorcb 
                
                time.sleep(1)
                
                gcode = gcoder.GCode(gcFile)
                
                p.startprint(gcode)                
                print "done printing?"

        except IOError:
                print "Failed to open gcode file: " + path_to_file
                
