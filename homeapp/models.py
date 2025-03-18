from django.db import models

# Create your models here.
class Emp_add(models.Model):
    emp_id=models.CharField(max_length=100)
    fname=models.CharField(max_length=100)
    mname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    add=models.CharField(max_length=1500)
    zip=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    idproof=models.CharField(max_length=100)
    working=models.BooleanField(default=True)

    #def __str__(self):
    #    return self.name

