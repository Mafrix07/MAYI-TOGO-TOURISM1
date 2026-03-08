from django.db import models
from django.conf import settings

class Recommandation(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    
    # Lien vers l'utilisateur à qui on recommande (ou qui a créé la recommandation)
    utilisateur = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='mes_recommandations'
    )
    
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre

    class Meta:
        verbose_name = "Recommandation"
        verbose_name_plural = "Recommandations"
