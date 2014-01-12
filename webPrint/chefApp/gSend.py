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

	def tempcb(self, data):
		print "temp --> " + data

        def errorcb(self, data):
                print "error--> " + data

	def sendcb(self, data):
		print "send --> " + data

	def preprintsendcb(self, gline, nextgline):
		if (gline != None) and (nextgline != None):
			#print "preprintsend --> "
			#print "\tline = " + gline.raw
			#print "\tnextline = " + nextgline.raw
			return gline

	def printsendcb(self, gline):
		if (gline != None):
			#print "printsend --> "
			print "\tline = " + gline.raw
		
			#Note: it seems that the total num of layers is broken in printcore 
	def layerchangecb(self, data):
		#print "layerchange --> %d" % (data, ) 
		print "layerchange --> %d/%d" % (data, self.device.analyzer.num_layers()) 

	def startcb(self, data):
		print "start --> Resuming=" + str(data)

	def endcb(self):
		print "end()"
	        #self.device.disconnect()

	def onlinecb(self, data):
		print "online --> " + data

        def replycb(self, data):
                #print "reply--> " + data
                
                if self.device == None:
                        print "device is not defined"
                        
                if self.device.queueindex > 0: 
                        pcnt = (100 * float(self.device.queueindex) / len(self.device.mainqueue)) 
                        print "%f complete" % pcnt
                                
                        if self.current_printer != None:
                                self.current_printer.state = "Printing"
                                self.current_printer.percent_complete = pcnt
                                self.current_printer.save()
                else:
                        print "q index = %d" % self.queueindex

        def printGcodeFile(self, path_to_file):
                sys.path.insert(0, '/home/corey/git/Printrun')
                from printrun import gcoder
                from printrun import printcore

                #for testing
                path_to_file = "/home/corey/100actions.gcode"
                #path_to_file = "/home/corey/test1.gcode"
                
                #default printer
                plist = Printer.objects.all()
                
                if(len(plist) > 0):
                        self.current_printer = plist[0]
                        
                try:
                        #print "printing gcode for " + path_to_file
                        gcFile = open(path_to_file, "rU")
                        
                        self.device = printcore.printcore('/dev/ttyUSB0', 115200)
                        self.device.recvcb = self.replycb
                        self.device.errorcb = self.errorcb 

			self.device.startcb = self.startcb
			self.device.endcb = self.endcb
			self.device.sendcb = self.sendcb
			self.device.onlinecb = self.onlinecb
			self.device.preprintsendcb = self.preprintsendcb
			self.device.printsendcb = self.printsendcb
			self.device.layerchangecb = self.layerchangecb
                        
                        time.sleep(1)
                        
                        gcode = gcoder.GCode(gcFile)
                        
                        self.device.startprint(gcode)                
                        print "done printing?"
			
                        
                except IOError:
                        print "Failed to open gcode file: " + path_to_file
                                
		except Exception:
			print "Some kind of exception happened"
