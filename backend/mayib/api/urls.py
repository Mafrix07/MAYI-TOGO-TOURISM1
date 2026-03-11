from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import ServiceViewSet, ReservationViewSet, TicketSupportViewSet, AvisViewSet

router = DefaultRouter()
router.register(r'services', ServiceViewSet, basename='service')
router.register(r'reservations', ReservationViewSet, basename='reservation')
router.register(r'support', TicketSupportViewSet, basename='support')
router.register(r'avis', AvisViewSet, basename='avis')

urlpatterns = [
    path('', include(router.urls)),
]
