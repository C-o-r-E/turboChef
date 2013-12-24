import sys
import time
from printrun.printcore import printcore
from printrun import gcoder

#############
# Callbacks
#############

def errorcb(data):
	print "error--> " + data

def replycb(data):
	print "reply--> " + data

	if p.queueindex > 0: 
		print "%f complete" % (100 * float(p.queueindex) / len(p.mainqueue)) 




p=printcore('/dev/ttyUSB0', 115200)
p.recvcb = replycb
p.errorcb = errorcb

time.sleep(1)

print "ready? lets try loading our file"

gcode = gcoder.GCode(open("100actions.gcode", "rU"))

print "Now lets print!!"

p.startprint(gcode)

time.sleep(1)

p.disconnect()
