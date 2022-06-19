from re import template
from django.views.generic import View, TemplateView, ListView, DetailView
from django.shortcuts import render
from . models import Imges
class Index(ListView):
 
 template_name = 'index.html'


 model = Imges


class Index2(ListView):
 
 template_name = 'help.html'


 model = Imges

class detailsDetailView(DetailView):
    template_name="details.html"
    model = Imges
    context_object_name = 'Imges'
