from django.db import models
from django.conf import settings

# Create your models here.


# Modèle de base pour les tickets de support
class TicketSupport(models.Model):
    STATUT_CHOICES = [
        ('OUVERT', 'Ouvert'),
        ('EN_COURS', 'En cours de traitement'),
        ('RESOLU', 'Résolu'),
        ('FERME', 'Fermé'),
    ]

    sujet = models.CharField(max_length=200)
    message = models.TextField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='OUVERT')
    date_ouverture = models.DateTimeField(auto_now_add=True)
    
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mes_tickets')
    agent_support = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='tickets_assignes',
        limit_choices_to={'role': 'support'}
    )

    def __str__(self):
        return f"Ticket #{self.id} - {self.sujet}"

    class Meta:
        verbose_name = "Ticket Support"
        verbose_name_plural = "Tickets Support"


# Modèle de base pour les services
class Service(models.Model):
    CATEGORIE_CHOICES = [
        ('HOTEL', 'Hébergement / Hôtel'),
        ('RESTO', 'Restauration / Snack'),
        ('GUIDE', 'Guide Touristique'),
        ('TRANSPORT', 'Transport / Location'),
        ('LOISIR', 'Loisir / Activité'),
    ]

    titre = models.CharField(max_length=200)
    description = models.TextField()
    categorie = models.CharField(max_length=20, choices=CATEGORIE_CHOICES)
    
    # Finances
    prix_total = models.DecimalField(max_digits=10, decimal_places=2, help_text="Prix total du service en FCFA")
    montant_acompte = models.DecimalField(max_digits=10, decimal_places=2, help_text="Montant de l'acompte (ticket d'entrée)")
    
    # Localisation
    adresse = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    
    # Médias
    image_principale = models.ImageField(upload_to='services/images/', null=True, blank=True)
    
    # Relations et Gestion
    prestataire = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='services_proposes',
        limit_choices_to={'role': 'pro'}
    )
    est_valide = models.BooleanField(default=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.titre} ({self.get_categorie_display()})"

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

# Modèle de base pour les événements
class Evenement(models.Model):
    nom = models.CharField(max_length=200)
    lieu = models.CharField(max_length=255)
    date_evenement = models.DateTimeField()
    description = models.TextField(blank=True)
    
    createur = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='evenements_crees'
    )
    services_associes = models.ManyToManyField(Service, related_name='evenements', blank=True)
    
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.date_evenement.strftime('%d/%m/%Y')}"

    class Meta:
        verbose_name = "Événement"
        verbose_name_plural = "Événements"

# Modèle de base pour les avis
class Avis(models.Model):
    note = models.PositiveSmallIntegerField(help_text="Note de 1 à 5")
    commentaire = models.TextField()
    date_avis = models.DateTimeField(auto_now_add=True)
    
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mes_avis')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='avis_clients')

    def __str__(self):
        return f"Avis {self.note}/5 par {self.utilisateur.username}"

    class Meta:
        verbose_name = "Avis"
        verbose_name_plural = "Avis"



# Modèle de base pour les réservations
class Reservation(models.Model):
    STATUT_CHOICES = [
        ('ATTENTE', 'En attente de paiement'),
        ('CONFIRME', 'Confirmée (Acompte payé)'),
        ('ANNULE', 'Annulée'),
        ('TERMINE', 'Service rendu'),
    ]

    touriste = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mes_reservations')
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='reservations_recues')
    date_reservation = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='ATTENTE')
    
    # Suivi financier basé sur le diagramme et notre discussion
    montant_total = models.DecimalField(max_digits=10, decimal_places=2)
    acompte_paye = models.BooleanField(default=False)
    code_ticket = models.CharField(max_length=20, unique=True, null=True, blank=True)

    def __str__(self):
        return f"Resa #{self.id} - {self.touriste.username} ({self.service.titre})"

    class Meta:
        verbose_name = "Réservation"
        verbose_name_plural = "Réservations"
