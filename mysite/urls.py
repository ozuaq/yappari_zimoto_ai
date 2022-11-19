from django.urls import path

from . import views

app_name = 'mysite'

urlpatterns = [
   path('zoom_out_map/', views.zoom_out_map_view, name='zoom_out_map'),
   path('modal_test', views.modal_test, name='modal_test'),
]