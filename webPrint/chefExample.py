import time
from chefApp.models import Printer

print "remember to make sure DJANGO_SETTINGS_MODULE env var is set..."

time.sleep(2)

p = Printer.objects.get(name__startswith='Test')


print "Simulating percentage:"

count = 0

while count <= 99:
	print "%d%% complete" % count
	count = count + 1
	p.percent_complete = count
	p.save()
	time.sleep(0.25)


print "done"
