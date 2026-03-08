from django.contrib import admin
from core.models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'prix_total', 'montant_acompte', 'prestataire', 'est_valide', 'date_creation')
    list_filter = ('categorie', 'est_valide', 'date_creation')
    search_fields = ('titre', 'description', 'adresse', 'prestataire__username')
    actions = ['valider_services']

    def valider_services(self, request, queryset):
        queryset.update(est_valide=True)
    valider_services.short_description = "Valider les services sélectionnés"
