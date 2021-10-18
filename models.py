from django.db import models

class Details (models.Model):
    name= models.CharField(max_length= 25)
    Email_id = models.CharField(max_length= 25)


def __str__(self):
    return self.name 
