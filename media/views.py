from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Person
def objectcreate(request):
    obj1 = Person()
    obj2 = Person()
    obj3 = Person()
    obj4 = Person()















    # Person.objects.create(name="Fahad",age="25", birth_date="29/06/1995",address="sreepur,Gazipur")
