from io import RawIOBase
from django import forms
from .models import Rapport, These,Publication,PlanEvaluation,AffectationJury,EvaluationJury

class TheseForm(forms.ModelForm):
    class Meta:
        model =  These
        fields = [
            'Title', 
            'Discription'
            ]

class PublicationForm(forms.ModelForm):
    class Meta:
        model =  Publication
        fields = [
            'name', 
            'date',
            'jury',
            'doctorant',
            'reveu',
            'url',
            'rang'
            ]

class LanceEvalForm(forms.ModelForm):
    class Meta:
        model =  PlanEvaluation
        fields = [
            'ddl',
            'moisPresnt',
            'lanceEval'
        ]

class SoumRapportForm(forms.ModelForm):
    class Meta:
        model =  Rapport
        fields = [
            'Intitule',
            'Prioritaire',
            'Discription',
            'doc'
        ]

class EvaluerForm(forms.ModelForm):
    class Meta:
        model =  Rapport
        fields = [
            'Commentaire',
        ]

class AffectJuryForm(forms.ModelForm):
    class Meta:
        model =  AffectationJury
        fields = [
            'doctorant',
            'JuryOne',
            'JuryTwo',
        ]


class EvaluationJuryForm(forms.ModelForm):
    class Meta:
        model =  EvaluationJury
        fields = [
            'doctorant',
            'evaluation',
            'Commontaire',
        ]