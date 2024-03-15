from django.urls import path
from .views import AbjadCalculateFA
urlpatterns = [
    path('abjad-calculate/', AbjadCalculateFA.as_view())
]