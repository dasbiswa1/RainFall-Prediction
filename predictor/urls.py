from django.urls import path
from . import views

urlpatterns=[
    path('index/',views.index,name="predictor-index"),
    path('about/',views.about,name="predictor-about"),
    path('contact/',views.contact,name="predictor-contact"),
    path('input/',views.input,name="predictor-input"),
    path('ot/',views.output,name="predictor-output"),
]