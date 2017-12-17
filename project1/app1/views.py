#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    """ Exemple de page HTML, Hello World """
    text = """<h1>Première page </h1>
              <p>Hello world !</p>"""
    return HttpResponse(text)
