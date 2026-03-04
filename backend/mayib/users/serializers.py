from rest_framework import serializers
from .models import * 


class UtilisateurSerializer(serializers.ModelSerializer):
    # j'ai ajouté le mot de passe manuellemeent car il doit être haché 

    password = serializers.CharField(write_only=True)

    class Meta : 
        model = Utilisateur
        fields = ['id', 'username', 'email', 'password', 'role', 'phone']
    
