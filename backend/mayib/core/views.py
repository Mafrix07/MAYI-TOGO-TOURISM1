from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import transaction
from .models import Service, Reservation, TicketSupport, Evenement, Avis, Recommandation
from .serializers import *

# ====================================================================================================
# SERVICES
# ====================================================================================================

class ServiceViewSet(viewsets.ModelViewSet):
    """Tout le monde peut voir les services validés, seuls les pros créent les leurs"""
    serializer_class = ServiceSerializer

    def get_queryset(self):
        if self.action == 'list':
            return Service.objects.filter(est_valide=True)
        return Service.objects.all()

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(prestataire=self.request.user)

# ====================================================================================================
# RÉSERVATIONS (Logique Métier)
# ====================================================================================================

class ReservationViewSet(viewsets.ModelViewSet):
    """Un touriste ne voit que ses réservations, un pro voit celles de ses services"""
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'touriste':
            return Reservation.objects.filter(touriste=user)
        elif user.role == 'pro':
            return Reservation.objects.filter(service__prestataire=user)
        return Reservation.objects.all()

    def create(self, request, *args, **kwargs):
        service_id = request.data.get('service')
        try:
            service = Service.objects.get(id=service_id)
            with transaction.atomic():
                reservation = Reservation.objects.create(
                    touriste=request.user,
                    service=service,
                    montant_total=service.prix_total,
                    statut='ATTENTE'
                )
                serializer = self.get_serializer(reservation)
                return Response({
                    "success": True,
                    "message": "Réservation créée avec succès.",
                    "data": serializer.data
                }, status=status.HTTP_201_CREATED)
        except Service.DoesNotExist:
            return Response({"error": "Service non trouvé"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

# ====================================================================================================
# AUTRES (Support, Avis, etc.)
# ====================================================================================================

class TicketSupportViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSupportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return TicketSupport.objects.filter(utilisateur=self.request.user)

    def perform_create(self, serializer):
        serializer.save(utilisateur=self.request.user)

class AvisViewSet(viewsets.ModelViewSet):
    serializer_class = AvisSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(utilisateur=self.request.user)
