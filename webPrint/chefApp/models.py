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

class CADFile(models.Model):
	name = models.CharField(max_length=100)
	full_path = model.CharField(max_length=200)
	status_msg = model.CharField(max_length=200)
	path_to_gcode = model.CharField(max_lenth=200)
	upload_time = models.DateTimeField('Uploaded at')
	cadfile = models.FileField(upload_to='cad_files/%Y/%m/%d')
