from rest_framework import serializers
from .models import TicketSupport, Service, Evenement, Avis, Reservation, Recommandation

class ServiceSerializer(serializers.ModelSerializer):
    prestataire_nom = serializers.ReadOnlyField(source='prestataire.username')
    categorie_display = serializers.CharField(source='get_categorie_display', read_only=True)

    class Meta:
        model = Service
        fields = (
            'id', 'titre', 'description', 'categorie', 'categorie_display', 
            'prix_total', 'montant_acompte', 'adresse', 'latitude', 'longitude', 
            'image_principale', 'prestataire', 'prestataire_nom', 'est_valide', 
            'date_creation'
        )

class ReservationSerializer(serializers.ModelSerializer):
    touriste_nom = serializers.ReadOnlyField(source='touriste.username')
    service_details = ServiceSerializer(source='service', read_only=True)
    statut_display = serializers.CharField(source='get_statut_display', read_only=True)

    class Meta:
        model = Reservation
        fields = (
            'id', 'touriste', 'touriste_nom', 'service', 'service_details', 
            'date_reservation', 'statut', 'statut_display', 'montant_total', 
            'acompte_paye', 'code_ticket'
        )

class AvisSerializer(serializers.ModelSerializer):
    utilisateur_nom = serializers.ReadOnlyField(source='utilisateur.username')

    class Meta:
        model = Avis
        fields = ('id', 'note', 'commentaire', 'date_avis', 'utilisateur', 'utilisateur_nom', 'service')

class TicketSupportSerializer(serializers.ModelSerializer):
    utilisateur_nom = serializers.ReadOnlyField(source='utilisateur.username')
    agent_nom = serializers.ReadOnlyField(source='agent_support.username')

    class Meta:
        model = TicketSupport
        fields = ('id', 'sujet', 'message', 'statut', 'date_ouverture', 'utilisateur', 'utilisateur_nom', 'agent_support', 'agent_nom')

class EvenementSerializer(serializers.ModelSerializer):
    createur_nom = serializers.ReadOnlyField(source='createur.username')

    class Meta:
        model = Evenement
        fields = ('id', 'nom', 'lieu', 'date_evenement', 'description', 'createur', 'createur_nom', 'services_associes', 'date_creation')

class RecommandationSerializer(serializers.ModelSerializer):
    utilisateur_nom = serializers.ReadOnlyField(source='utilisateur.username')

    class Meta:
        model = Recommandation
        fields = ('id', 'titre', 'description', 'utilisateur', 'utilisateur_nom', 'date_publication')
