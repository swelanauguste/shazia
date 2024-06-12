from django.urls import path

from .views import UnitListView, UnitCreateView, UnitDetailView, UnitUpdateView


urlpatterns = [
    path('', UnitListView.as_view(), name='list'),
    path('add/', UnitCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', UnitDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', UnitUpdateView.as_view(), name='update'),
]
