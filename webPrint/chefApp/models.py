from django.db import models

#Note: for transition to python3, may need to change __unicode__ to __str__

class Printer(models.Model):
	name = models.CharField(max_length=200)
	percent_complete = models.IntegerField(default=0)
	state = models.CharField(max_length=200)
	last_start = models.DateTimeField('Last started running')
	last_stop = models.DateTimeField('Last stopped running')

	def __unicode__(self):
		return self.name


class Material(models.Model):
	name = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.name


class Extruder(models.Model):
	printer = models.ForeignKey(Printer)
	current_temp = models.IntegerField(default=0)
	max_temp = models.IntegerField(default=0)
	name = models.CharField(max_length=200)
	material = models.OneToOneField(Material)

	def __unicode__(self):
		return self.name


