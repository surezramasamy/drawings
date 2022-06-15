from django.shortcuts import render,redirect
from django.views.generic import ListView,CreateView
from .models import Drawings_2D,Model_Name
from .forms import drgform,drguploadform
import pandas
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.core.exceptions import FieldDoesNotExist

class HomePageView(ListView):
    model = Drawings_2D
    template_name = 'home.html'



def drgupload(request):
    if request.method == 'POST':
        form = drguploadform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = drguploadform()
    return render(request, 'drgupload.html', {
        'form': form
    })



def drg(request):
    drg_qs = None
    search_form = drgform(request.POST or None)
    if request.method == 'POST':
        Model_Name = request.POST.get('Model_Name')
        Sub_Assembly_Name = request.POST.get('Sub_Assembly_Name')
        drg_qs = Drawings_2D.objects.filter(Model_Name=Model_Name, Sub_Assembly_Name=Sub_Assembly_Name)

    context = {
        'search_form': search_form,
        'drg_qs': drg_qs,


    }
    return render(request, 'drg.html',  context)
