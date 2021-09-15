"""DPGRtalents URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from users import views as user_views
from app import views as app_views
from django.conf.urls.static import static
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('profile/',user_views.profile,name='profile'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    ####
    path('lance_eval/',app_views.lance_eval_view,name='lance_eval_view'),
    path('affct_jury/',app_views.affct_jury_view,name='affct_jury_view'),
    path('affct_jury_list/',app_views.affectation_list_view,name='affectation_list_view'),
    #Doctorant
    path('soum_rpprt/',app_views.soum_rpprt_view,name='soum_rpprt_view'),
    #ENS
    path('ens_evals_list/',app_views.ensevals_list_view,name='ensevals_list_view'),
    path('eval_rpprt/',app_views.evaluer_rpprt_view,name='evaluer_rpprt_view'),
    path('ev_comments/',app_views.EvaluationJury_list_view,name='EvaluationJury_list_view'),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
