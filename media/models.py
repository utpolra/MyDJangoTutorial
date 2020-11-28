from django.db import models
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    birth_date=models.CharField(max_length=100)
    address=models.CharField(max_length=100)