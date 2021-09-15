from django.http.response import Http404
from .forms import TheseForm,PublicationForm,LanceEvalForm,SoumRapportForm,AffectJuryForm,EvaluerForm,EvaluationJuryForm
from .models import AffectationJury,Rapport,EvaluationJury
from django.shortcuts import render
from django.conf import settings
import os
from django.http import HttpResponse
from django.views.generic import (TemplateView,
                                    ListView,
                                    DetailView,
                                    CreateView,
                                    UpdateView, 
                                    DeleteView)
# Create your views here.

def home(request):
    return render(request,"base.html")

def commentaires(request):
    return render(request,"commentaires.html")

def pub_create_view(request):
    form = PublicationForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'pub_form': form
    }
    return render(request, "profil.html", context)

    
def these_create_view(request):
    form = TheseForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'th_form': form
    }
    return render(request, "depotRapport.html", context)


def lance_eval_view(request):
    form = LanceEvalForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'ev_form': form
    }
    return render(request, "lanceEval.html", context)

def soum_rpprt_view(request):
    form = SoumRapportForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
    context = {
        'rpprt_form': form
    }
    return render(request, "depotRapport.html", context)

def affct_jury_view(request):
    form = AffectJuryForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'affjry_form': form
    }
    return render(request, "Affectation.html", context)

def affectation_list_view(request):
    queryset = AffectationJury.objects.all()
    context = {
        "object_list" : queryset
    }
    return render(request, "affectationList.html", context)


def EvaluationJury_list_view(request):
    queryset = EvaluationJury.objects.all()
    context = {
        "eval_jry_list" : queryset
    }
    return render(request, "users/commentaires.html", context)

def ensevals_list_view(request):
    queryset = Rapport.objects.all()
    context = {
        "enseval_list" : queryset
    }
    return render(request, "EnsEvalList.html", context)

def download(request, path):
    fs = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(fs):
        with fs.open(fs) as fh:
            response = HttpResponse(fh.read(), content_type='application/doc')
            response['Content-Disposition'] = 'inline; filename=os.path.join(settings.MEDIA_ROOT,path)'
            return response
    
    raise Http404('The requested pdf was not found in our server.')

class RapportUpdateView(UpdateView):
    model = Rapport
    template_name = "evaluer.html"
    fields = ['Commentaire']

def RapportEvalView(request, slug):
    eval = Rapport.objects.get(RPPRTslug=slug)
    context ={'eval' : eval}
    return render(request, 'evaluer.html', context)


def evaluer_rpprt_view(request):
    form = EvaluationJuryForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'eval_rpprt_form': form
    }
    return render(request, "evaluer.html", context)


