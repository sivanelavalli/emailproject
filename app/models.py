from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    contactno=models.IntegerField()
    email=models.EmailField(max_length=100,primary_key=True)
    password=models.CharField(max_length=20)
    image=models.ImageField(upload_to='my_images',default=False)
