# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'plateforme/index.html')

def presentation(request):
    return HttpResponse('ja suis la presentation de la JAPSSO')
