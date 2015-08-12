from django.db import models

# Create your models here.

class City(models.Model):
	name = models.CharField(max_length=30, null=True)
	county = models.CharField(max_length=30, null=True)
	zip_code = models.IntegerField(null=True)
	latitude = models.FloatField(null=True)
	longitude = models.FloatField(null=True)
	state = models.ForeignKey('maim.State', null=True)

	def __unicode__(self):
		return self.name

class StateCapital(models.Model):
	name = models.CharField(max_length=30, unique=True)
	latitude = models.FloatField(null=True)
	longitude = models.FloatField(null=True)
	population = models.IntegerField(null=True)
	state = models.OneToOneField("maim.State", null=True)

	def __unicode__(self):
		return self.name

class State(models.Model):
	name = models.CharField(max_length=30, unique=True)
	abbreviation = models.CharField(max_length=2, null=True)
	
	def upper(self):
		name_string = str(self.name)
		return name_string.upper()

	def make_stuff(self, made_up_stuff):
		stuff_string = "%s ,%s" % (self.name, made_up_stuff)
		return name_string.upper()

	def __unicode__(self):
		return self.name

	

#class StateAdmin(admin.ModelAdmin):
	#list_display = ('name', 'abbreviation', 'capital', ) 
	#search_fields = ['name']
