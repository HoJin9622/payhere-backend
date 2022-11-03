from django.urls import path
from . import views

urlpatterns = [
    path("", views.HouseholdDetailView.as_view()),
    path("<int:pk>/", views.HouseholdsView.as_view()),
]
