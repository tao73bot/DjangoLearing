from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_taohid, name='all_taohid'),
    path('<int:id>/', views.taohid_detail, name='taohid_detail'),
    path('taohid_stores/', views.taohid_store_view, name='taohid_stores')
]
