from django.shortcuts import render
from myapp.models import Employee
from django.views.generic import *
from django.urls import reverse_lazy
class EmployeeView(ListView):
    model=Employee

class EmployeeDetailView(DetailView):
    model=Employee

class EmployeeCreateView(CreateView):
    model=Employee
    fields='__all__'

class EmployeeUpdateView(UpdateView):
    model=Employee
    fields=('edesig','eexp','esal')

class EmployeeDeleteView(DeleteView):
    model=Employee
    success_url=reverse_lazy('employeeList')
