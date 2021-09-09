from django.urls import path
from . import views

urlpatterns = [
    path('secret/', views.addSecret, name="add-secret"),
    path('secret/<str:_hash>', views.getSecret, name="get-secret")
]