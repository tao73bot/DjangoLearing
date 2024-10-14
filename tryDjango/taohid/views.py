from django.shortcuts import render
from .models import TaoihdDetails
from django.shortcuts import get_list_or_404
# Create your views here.
def all_taohid(request):
    taohids = TaoihdDetails.objects.all()
    return render(request, 'taohid/all_taohid.html', {'taohids': taohids})

def taohid_detail(request, id):
    taohid = get_list_or_404(TaoihdDetails, pk=id)
    return render(request, 'taohid/taohid_detail.html', {'taohid': taohid})