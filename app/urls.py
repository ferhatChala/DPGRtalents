from django.urls import path,include
from . import views

app_name='app'
urlpatterns = [
    path('',views.home,name='home'),
    #path('create_th/',views.these_create_view,name='these_create_view'),
    #path('create_pub/',views.pub_create_view,name='pub_create_view'),
    
    
]