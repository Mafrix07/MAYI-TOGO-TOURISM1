from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Utilisateur

@admin.register(Utilisateur)
class UtilisateurAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'phone', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Informations MAYI', {'fields': ('role', 'phone')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informations MAYI', {'fields': ('role', 'phone')}),
    )
