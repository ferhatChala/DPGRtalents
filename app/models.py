from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse

class These(models.Model):
    Title = models.CharField(max_length=20,verbose_name=_('These name '))
    Discription = models.TextField(max_length=500,verbose_name=_('These Discription '))

    def __str__(self):
        return self.Title

class Travaille(models.Model):
    name = models.CharField(max_length=20,verbose_name=_('Le Travaille'))
    description = models.TextField(max_length=20,verbose_name=_('Discription'))
    date = models.DateTimeField(verbose_name=_('La date du travaille '))
    jury =  models.ForeignKey('users.DThese',related_name='jurys',on_delete=models.CASCADE,verbose_name=_('Le jury '))
    doctorant =  models.ForeignKey('users.Doctorant',related_name='travaux',on_delete=models.CASCADE,verbose_name=_('Le Doctorant'))

    def __str__(self):
        return self.name


class Semminaire(Travaille):
    lieu = models.CharField(max_length=20,verbose_name=_('Lieu'))

    def __str__(self):
        return self.name

class Conference(Travaille):
    lieu = models.CharField(max_length=20,verbose_name=_('Lieu'))

    def __str__(self):
        return self.name

class Publication(Travaille):
    reveu = models.CharField(max_length=20,verbose_name=_('Reveu de la publication'))
    url = models.CharField(max_length=20,verbose_name=_('Le lien de publication'))
    rang = models.CharField(max_length=20,verbose_name=_('Le rang de publication'))

    def __str__(self):
        return self.name

class Module(Travaille):
    dure = models.IntegerField(verbose_name=_('Le Module'))

    def __str__(self):
        return self.name

class Brevet(Travaille):
    degre = models.CharField(max_length=20,verbose_name=_('Degre de brevet'))

    def __str__(self):
        return self.name



class Certaficat(models.Model):
    CRTFdate = models.DateTimeField(verbose_name=_('La date de creation '))
    CRTFdoctorant =  models.ForeignKey('users.Doctorant',on_delete=models.CASCADE,verbose_name=_('Le Doctorant crtf'))
    CRTFanneUniv = models.IntegerField(_("Annee universitaire "))
    CRTFniveau = models.IntegerField(_("Niveau"))


    def __str__(self):
        return self.doctorant


class Rapport(models.Model):
    pk = int
    Intitule = models.ForeignKey('app.These', on_delete=models.CASCADE)
    Prioritaire = models.ForeignKey("users.Doctorant", verbose_name=_("Prioritaire"), on_delete=models.CASCADE)
    Discription = models.TextField(_("Discription de rapport"))
    doc = models.FileField(_("doc"), upload_to='Media', max_length=100)

    Commentaire = models.TextField(_("Evaluer le rapport"),default=".")

    RPPRTslug = models.SlugField(blank=True, null=True)

    def save(self, *args,**kwargs):
        if not self.RPPRTslug :
            self.RPPRTslug = slugify(self.Intitule.Title)
        super(Rapport, self).save(*args,**kwargs)


    def get_absolute_url(self):
        return reverse('author-detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.Intitule.Title

class PlanEvaluation(models.Model):
    ddl = models.DateField(_("Fixer la date limit pour la soumission des rapport"), auto_now=False, auto_now_add=False)
    moisPresnt = models.DateField(_("Fixer le mois de les presentation"), auto_now=False, auto_now_add=False)
    lanceEval = models.BooleanField(_("Lancer"), )

class AffectationJury(models.Model):
    doctorant =  models.ForeignKey('users.Doctorant',on_delete=models.CASCADE,verbose_name=_('Le Doctorant '))
    JuryOne = models.ForeignKey('users.Teacher', related_name='JuryOne',verbose_name=_("Selectionner le 1er jury "), on_delete=models.CASCADE)
    JuryTwo = models.ForeignKey('users.Teacher', related_name='JuryTwo',verbose_name=_("Selectionner le 2er jury "), on_delete=models.CASCADE)


    def __str__(self):
        return self.doctorant.nom


class EvaluationJury(models.Model):
    doctorant =  models.ForeignKey('users.Doctorant',on_delete=models.CASCADE,verbose_name=_('Le Doctorant '))
    evaluation = models.ForeignKey('app.evaluation', on_delete=models.CASCADE)
    Commontaire = models.TextField(max_length=20,verbose_name=_('Evaluer le rapport'))

    def __str__(self):
        return self.doctorant.nom


class Evaluation(models.Model):
    ev = models.CharField(max_length=20,verbose_name=_('Eval'))

    def __str__(self):
        return self.ev
