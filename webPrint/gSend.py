import sys
import time
from printrun.printcore import printcore
from printrun import gcoder



def errorcb(data):
	print "error--> " + data

def replycb(data):
	print "reply--> " + data

	if p.queueindex > 0: 
		print "%f complete" % (100 * float(p.queueindex) / len(p.mainqueue)) 







p=printcore(sys.argv[1], 115200)
p.recvcb = replycb
p.errorcb = errorcb

time.sleep(1)

print "ready? lets try loading our file"

gcode = gcoder.GCode(open("100actions.gcode", "rU"))

print "Dimensions:"
xdims = (gcode.xmin, gcode.xmax, gcode.width)
print "\tX: %0.02f - %0.02f (%0.02f)" % xdims
ydims = (gcode.ymin, gcode.ymax, gcode.depth)
print "\tY: %0.02f - %0.02f (%0.02f)" % ydims
zdims = (gcode.zmin, gcode.zmax, gcode.height)
print "\tZ: %0.02f - %0.02f (%0.02f)" % zdims
print "Filament used: %0.02fmm" % gcode.filament_length
print "Number of layers: %d" % gcode.num_layers()
print "Estimated duration: %s" % gcode.estimate_duration()


print "Now lets print!!"

p.startprint(gcode)

time.sleep(1)

#while p.printing:
#	print "f% complete" % 100 * float(p.queueindex) / len(p.mainqueue) 
#	time.sleep(1)




#p.startprint(data) # data is an array of gcode lines
#p.send_now("M105") # sends M105 as soon as possible
#p.pause()
#p.resume()
#p.disconnect()
