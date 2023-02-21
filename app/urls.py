from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'), 
    path('insert', views.insert, name='insert'),
    path('update/<id>', views.update, name='update'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('download', views.download, name='download'),
    path('delete/<id>', views.delete, name='delete'),
]