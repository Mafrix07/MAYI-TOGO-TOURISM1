from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here. 

class Utilisateur(AbstractUser):

    ADMIN = 'admin'
    TOURISTE = 'touriste'
    PRO = 'pro'
    SUPPORT = 'support'

    ROLE_CHOICES = (
        (ADMIN, 'Administrateur'),
        (TOURISTE, 'Touriste'),
        (PRO, 'Professionnel'),
        (SUPPORT, 'Support Client'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=TOURISTE)
    phone = models.CharField(max_length=20, blank=True, null=True)

    @property
    def is_admin_role(self):
        return self.role == self.ADMIN

    @property
    def is_touriste(self):
        return self.role == self.TOURISTE

    @property
    def is_pro(self):
        return self.role == self.PRO

    @property
    def is_support(self):
        return self.role == self.SUPPORT

    def __str__(self):
        return f"{self.username} ({self.role})"