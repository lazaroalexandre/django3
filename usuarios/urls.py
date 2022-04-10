from .views import UsuarioCreate
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name = 'usuarios/formulario.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('registrar/', UsuarioCreate.as_view(), name="registrar"),
]