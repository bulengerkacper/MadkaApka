from django.db import models
# Create your models here.

class Mother(models.Model):
	firstName = models.CharField(max_length=50)
	secondName = models.CharField(max_length=50)
	age = models.IntegerField()
	childs = models.IntegerField()
	money = models.FloatField(default=0)
	patoFace = models.ImageField(upload_to ='pic_folder/', default = 'pic_folder/None/no-img.jpg' )

	def __str__(self):
		return self.firstName + " " + self.secondName

class Child(models.Model):
	firstName = models.CharField(max_length=50)
	secondName = models.CharField(max_length=50)
	age = models.IntegerField()
	can500plus = models.BinaryField()
	isAlive = models.BinaryField()

	def __str__(self):
		return self.firstName + " " + self.secondName