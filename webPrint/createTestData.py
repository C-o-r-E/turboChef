import os
from chefApp.models import Printer
from django.utils import timezone

os.environ['DJANGO_SETTINGS_MODULE'] = 'chefApp.settings'


#create a new printer
p = Printer(name='testPrinter01')
p.last_start = timezone.now()
p.last_stop = timezone.now()
p.save()


#p = Printer.objects.get(name__startswith='Test')


#print "Simulating percentage:"

#count = 0

#while count <= 99:
#	print "%d%% complete" % count
#	count = count + 1
#	p.percent_complete = count
#	p.save()
#	time.sleep(0.25)


#print "done"
