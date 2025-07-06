from django.urls import path
from core.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",auth,name="auth"),
    path("register",register,name="register"),
    path("home",home,name="home"),
    # Password reset flow
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path("userlogout",userlogout,name="userlogout"),
    path("create_profile",create_profile,name="create_profile"),
    path("view_profile",view_profile,name="view_profile"),
    path("public_profile",public_profile,name="public_profile")
]
