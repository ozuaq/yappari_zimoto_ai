from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def zoom_out_map_view(request):
    return render(request, 'mysite/zoom_out_map.html')

def modal_test(request):
    return render(request, 'mysite/modal_test.html')