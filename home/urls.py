from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name= 'index' ),
    

    # path('delete/<int:id>/',views.delview, name='delete'),
    # path('uncomplete/<int:id>/',views.InComplete, name='InComplete'),
    # path('complete/<int:id>/',views.Complete, name='Complete'),
]