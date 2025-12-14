from django.urls import path
from .views import EquipoListView, EquipoDetailView

app_name = 'apps.nosotros'

urlpatterns = [
    path('nosotros/', EquipoListView.as_view(), name='nosotros'),
    path('nosotros/<int:pk>/', EquipoDetailView.as_view(), name= 'nosotros_individual')
]
