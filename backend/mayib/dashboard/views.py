from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from core.models import Service, Reservation, TicketSupport
from users.models import Utilisateur

class DashboardLoginView(LoginView):
    template_name = 'dashboard/login.html'
    redirect_authenticated_user = True

class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """Mixin pour restreindre l'accès aux administrateurs uniquement"""
    login_url = 'dashboard:login'

    def test_func(self):
        return self.request.user.role == 'admin'

class DashboardIndexView(AdminRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Statistiques globales
        context['total_users'] = Utilisateur.objects.count()
        context['total_services'] = Service.objects.count()
        context['total_reservations'] = Reservation.objects.count()
        context['total_tickets'] = TicketSupport.objects.count()
        
        # Réservations récentes (5 dernières)
        context['recent_reservations'] = Reservation.objects.select_related('touriste', 'service').order_by('-date_reservation')[:5]
        
        # Services en attente de validation
        context['pending_services'] = Service.objects.filter(est_valide=False).count()
        
        return context

class UserListView(AdminRequiredMixin, ListView):
    model = Utilisateur
    template_name = 'dashboard/users/list.html'
    context_object_name = 'users'
    paginate_by = 10
    ordering = ['-date_joined']

class UserDetailView(AdminRequiredMixin, DetailView):
    model = Utilisateur
    template_name = 'dashboard/users/detail.html'
    context_object_name = 'target_user'  # 'user' est réservé par Django pour l'utilisateur connecté

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # On peut ajouter les services si c'est un pro ou les réservations si c'est un touriste
        target = self.get_object()
        if target.role == 'pro':
            context['services'] = Service.objects.filter(prestataire=target)
        elif target.role == 'touriste':
            context['reservations'] = Reservation.objects.filter(touriste=target).select_related('service')
        
        return context
