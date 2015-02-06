from django.shortcuts import render
from .forms import SearchForm
# Create your views here.


def search_form(request):
    if requested.method == "POST":
        form = SearchForm(requested.POST)    
        if form.is_valid():
            org_1 = form.cleaned_data['org_1']
            org_2 = form.cleaned_data['org_1']
            dep_date = form.cleaned_data['dep_date']
            ret_date = form.cleaned_data['ret_date']
            ## Create trip object
            Place.objects.create()
            
    
    return render(request,'f2m_app/search_form.html',{'form':form})
