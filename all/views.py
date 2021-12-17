from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class AllView(TemplateView):
    template_name='all/all.html'