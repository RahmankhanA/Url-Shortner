from django.http import HttpResponse
from django.shortcuts import render, redirect
import random
from url.models import UrlData
from url.forms import Url
import string





def urlShort(request):
    if request.method == 'POST':
        form = Url(request.POST)
        if form.is_valid():
            slug = ''.join(random.choice(string.ascii_letters)
                           for x in range(10))
            url = form.cleaned_data["url"]
            try:
                queryset=UrlData.objects.get(url=url)
                return HttpResponse(queryset.slug)
            except Exception as e:
                new_url = UrlData(url=url, slug=slug)
                new_url.save()
                return HttpResponse(slug)
    else:
        form = Url()
    data = UrlData.objects.all()
    context = {
        'form': form,
        'data': data
    }
    return render(request, 'index.html', context)



def urlRedirect(request):
    if request.method == 'POST':
        form = Url(request.POST)
        if form.is_valid():
            slug=form.cleaned_data["url"]
            orignal_url = UrlData.objects.get(slug=slug)
            return HttpResponse(orignal_url.url)
        
    else:
        form = Url()
    context = {
        'form': form
      
    }
    return render(request, 'revert.html', context)
    
    # return redirect(data.url)
