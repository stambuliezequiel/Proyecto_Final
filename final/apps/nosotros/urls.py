from django.urls import path
from .views import EquipoListView, EquipoDetailView

urlpatterns = [
    path('nosotros/', EquipoListView.as_view(), name='nosotros'),
    path('nosotros/<int:id>/', EquipoDetailView.as_view(), name= 'nosotros_individual')
]
