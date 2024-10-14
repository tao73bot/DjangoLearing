from django.shortcuts import render
from .models import TaoihdDetails, TaohidReview, Store, TaohidContact
from django.shortcuts import get_list_or_404
from .forms import TaohidForm
# Create your views here.
def all_taohid(request):
    taohids = TaoihdDetails.objects.all()
    return render(request, 'taohid/all_taohid.html', {'taohids': taohids})

def taohid_detail(request, id):
    taohid = get_list_or_404(TaoihdDetails, pk=id)
    return render(request, 'taohid/taohid_detail.html', {'taohid': taohid})

def taohid_store_view(request):
    taohids = None
    if request.method == 'POST':
        form = TaohidForm(request.POST)
        if form.is_valid():
            taohid_details = form.cleaned_data['taohid_details']
            taohids = Store.objects.filter(taohid_details=taohid_details)
    else:
        form = TaohidForm()
    return render(request, 'taohid/taohid_stores.html', {'taohids': taohids}, {'form': form})