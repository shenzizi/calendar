from django.db import models

# Create your models here.
class Testing(models.Model):
	name = models.CharField(max_length=50,default="defaultvalue")
	phone = models.CharField(max_length=10,default="defaultvalue")
	comments = models.CharField(max_length=500,default="defaultvalue")
	submittedtime = models.DateTimeField(default=None,null=True,blank=True)
