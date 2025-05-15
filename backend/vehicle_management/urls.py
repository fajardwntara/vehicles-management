from django.urls import path
from .views import (
    MotorcycleListView,
    MotorcycleCreateView,
    MotorcycleUpdateView,
    MotorcycleDeleteView,

    CarListView,
    CarCreateView,
    CarUpdateView,
    CarDeleteView,
)

urlpatterns = [
    # motorcycles
    path('motorcycle/lists', MotorcycleListView.as_view(), name='v-motorcycle-lists'),
    path('motorcycle/create', MotorcycleCreateView.as_view(), name='v-motorcycle-create'),
    path('motorcycle/update/<int:pk>/', MotorcycleUpdateView.as_view(), name='v-motorcycle-update'),
    path('motorcycle/delete/<int:pk>/', MotorcycleDeleteView.as_view(), name='v-motorcycle-delete'),

    # cars
    path('car/lists', CarListView.as_view(), name='v-car-lists'),
    path('car/create', CarCreateView.as_view(), name='v-car-create'),
    path('car/update/<int:pk>/', CarUpdateView.as_view(), name='v-car-update'),
    path('car/delete/<int:pk>/', CarDeleteView.as_view(), name='v-car-delete'),

]