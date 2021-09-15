from django.shortcuts import render,redirect
from django.views.generic import (TemplateView,
                                    ListView,
                                    DetailView,
                                    CreateView,
                                    UpdateView, 
                                    DeleteView)
from django.contrib.auth.decorators import login_required
from .forms import ProfileUpdateForm
from .models import Doctorant,User

# Create your views here.
@login_required
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.doctorant)
        if  p_form.is_valid():
            p_form.save()
            return redirect('profile')

    else:
        p_form = ProfileUpdateForm(instance=request.user.doctorant)

    context = {
        'p_form': p_form
    }

    return render(request, 'users/profil.html', context)