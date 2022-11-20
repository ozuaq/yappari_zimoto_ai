from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import SpotInfo

# Create your views here.
def zoom_out_map_view(request):
    pin_list = []
    
    pins = SpotInfo.objects.all()
    for pin in pins:
        pin_list.append({'id': pin.id, 'name': pin.location_name, 'category': pin.category, 'time': pin.time, 'season': pin.season, 'tags': pin.tags, 'image': pin.image, 'appeal': pin.appeal, 'good': pin.good, 'visit': pin.visit, 'x': pin.position_x, 'y': pin.position_y})
    return render(request, 'mysite/zoom_out_map.html', {'pin_list': pin_list})

def modal_test(request):
    return render(request, 'mysite/modal_test.html')