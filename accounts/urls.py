from django.urls import path,include
from . import views
urlpatterns = [
    path('registration/',views.RegistrationView.as_view(),name='registration'),
    path('active/<uid64>/<token>/',views.activate,name="active"),
    path('login/',views.LoginView.as_view(),name='login'),
    path('logout/',views.LogoutView.as_view(),name='logout'),
    path('<int:pk>/',views.RegistrationDetailView.as_view()),
]