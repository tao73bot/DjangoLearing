from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_taohid, name='all_taohid'),
    path('<int:id>/', views.taohid_detail, name='taohid_detail')
]
