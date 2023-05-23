from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from app.models import *
from django.urls import reverse_lazy
# Create your views here.
class home(TemplateView):
    template_name='app/home.html'

class school_list(ListView):
    model=School
    #template_name='app/school_list.html'
    context_object_name='schools'
    ordering='name'

class SchoolDetail(DetailView):
    model=School
    context_object_name='sclobject'
    #template_name='SchoolDetail.html'

class SchoolCreate(CreateView):
    model=School
    fields='__all__'

class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'

class SchoolDelete(DeleteView):
    model=School
    context_object_name='schoolobject'
    success_url=reverse_lazy('school_list')
