from django.db import models
 
class team(models.Model):
    name= models.CharField(max_length=100)
    title= models.CharField(max_length=100)
    image = models.FileField(upload_to='images/',max_length=250,null=True,default=None)

    