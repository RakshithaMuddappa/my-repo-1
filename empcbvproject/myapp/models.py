from audioop import reverse
import imp
from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse
class Employee(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=10)
    edesig=models.CharField(max_length=10)
    eexp=models.IntegerField()
    esal=models.IntegerField()

    def __str__(self) :
        return self.ename
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
