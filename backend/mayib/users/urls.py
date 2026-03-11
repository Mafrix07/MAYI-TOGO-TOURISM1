from django.urls import path
from .views import InscriptionView, MonProfilView

urlpatterns = [
    path('inscription/', InscriptionView.as_view(), name='inscription'),
    path('me/', MonProfilView.as_view(), name='mon_profil'),
]
