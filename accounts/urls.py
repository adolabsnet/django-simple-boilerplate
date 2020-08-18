from django.urls import path

from .views import RegisterView, LoginView, LogoutView, DashboardView


urlpatterns = [
    path('register/', RegisterView, name='register'),
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView, name='logout'),
    path('dashboard/', DashboardView, name='dashboard'),
]
