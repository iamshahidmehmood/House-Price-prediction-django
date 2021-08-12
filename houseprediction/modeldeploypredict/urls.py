from django.urls import path
from  . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    #path("index/predict/",views.index, name="index"),
    path('predict/', views.prediction, name='predict'),
    path("predict/result/",views.result),
]