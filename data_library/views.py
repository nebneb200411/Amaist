from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import DataLibrary


class DataLibraryView(ListView):
    template_name = 'data_library/datas.html'
    model = DataLibrary
