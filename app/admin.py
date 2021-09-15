from django.contrib import admin
from .models import Rapport, Travaille,These,EvaluationJury,Evaluation,Semminaire,Conference,Publication,Module,Brevet,Certaficat,PlanEvaluation,AffectationJury


admin.site.register(Travaille)
admin.site.register(These)
admin.site.register(Semminaire)
admin.site.register(Conference)
admin.site.register(Publication)
admin.site.register(Module)
admin.site.register(Brevet)
admin.site.register(Certaficat)
admin.site.register(Rapport)
admin.site.register(PlanEvaluation)
admin.site.register(AffectationJury)
admin.site.register(Evaluation)
admin.site.register(EvaluationJury)