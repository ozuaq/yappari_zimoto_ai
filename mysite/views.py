from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def zoom_out_map_view(request):
    return render(request, 'mysite/map_zoomout.html')