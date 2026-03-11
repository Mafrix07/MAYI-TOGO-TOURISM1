from django.contrib import admin
from .models import Service, Reservation, TicketSupport, Evenement, Avis, Recommandation

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'prix_total', 'prestataire', 'est_valide')
    list_filter = ('categorie', 'est_valide', 'prestataire')
    search_fields = ('titre', 'description', 'adresse')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'touriste', 'service', 'statut', 'date_reservation', 'acompte_paye')
    list_filter = ('statut', 'acompte_paye')
    search_fields = ('touriste__username', 'service__titre', 'code_ticket')

@admin.register(TicketSupport)
class TicketSupportAdmin(admin.ModelAdmin):
    list_display = ('sujet', 'utilisateur', 'statut', 'date_ouverture', 'agent_support')
    list_filter = ('statut',)
    search_fields = ('sujet', 'message', 'utilisateur__username')

@admin.register(Avis)
class AvisAdmin(admin.ModelAdmin):
    list_display = ('service', 'utilisateur', 'note', 'date_avis')
    list_filter = ('note',)

admin.site.register(Evenement)
admin.site.register(Recommandation)
