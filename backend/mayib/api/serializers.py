from rest_framework import serializers
from .models import Recommandation

class RecommandationSerializer(serializers.ModelSerializer):
    utilisateur_nom = serializers.ReadOnlyField(source='utilisateur.username')

    class Meta:
        model = Recommandation
        fields = ['id', 'titre', 'description', 'utilisateur', 'utilisateur_nom', 'date_publication']
