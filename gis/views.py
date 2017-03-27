# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("GIS index.")
##from django.shortcuts import render_to_response
##
##def index (request):
##    #return render_to_response('C://Python27/KCCA/djangogis/gis/index.html')
##    fp = open('C://Python27/KCCA/djangogis/gis/index.html')
