from rest_framework import serializers
from .models import Utilisateur
from django.contrib.auth.password_validation import validate_password

class InscriptionSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Utilisateur
        fields = ('username', 'email', 'password', 'password_confirm', 'role', 'phone', 'first_name', 'last_name')

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "Les mots de passe ne correspondent pas."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = Utilisateur.objects.create_user(**validated_data)
        return user

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ('id', 'username', 'email', 'role', 'phone', 'first_name', 'last_name')
        read_only_fields = ('role',)
