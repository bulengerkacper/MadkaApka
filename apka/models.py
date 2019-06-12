from django.db import models
from django.db.models import Count
# Create your models here.

class Mother(models.Model):
	id = models.AutoField(primary_key=True)
	firstName = models.CharField(max_length=50)
	secondName = models.CharField(max_length=50)
	age = models.IntegerField()
	#childrens = models.IntegerField()
	money = models.FloatField(default=0)
	patoFace = models.ImageField(upload_to ='pic_folder/', default = 'pic_folder/None/no-img.jpg' )
	points = models.IntegerField(default=0)
	
	def __str__(self):
		return self.firstName + " " + self.secondName

	def getChildrenCount(self):
		childrens = Child.objects.filter(mother=self).count()
		print (childrens)

class Child(models.Model):
	id = models.AutoField(primary_key=True)
	firstName = models.CharField(max_length=50)
	secondName = models.CharField(max_length=50)
	age = models.IntegerField()
	can500plus = models.BinaryField()
	mother = models.ForeignKey(Mother, on_delete=models.PROTECT)
	isAlive = models.BinaryField()
	childrensFace = models.ImageField(upload_to ='pic_folder/', default = 'pic_folder/None/no-img.jpg' )

	def __str__(self):
		return self.firstName + " " + self.secondName