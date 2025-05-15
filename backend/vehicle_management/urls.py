from django.urls import path
from .views import (
    MotorcycleView,
    MotorcycleListView,
    MotorcycleCreateView,
    MotorcycleUpdateView,
    MotorcycleDeleteView
)

urlpatterns = [
    # motorcycles
    path('motorcycle/lists', MotorcycleListView.as_view(), name='v-motorcycle-lists'),
    path('motorcycle/create', MotorcycleCreateView.as_view(), name='v-motorcycle-create'),
    path('motorcycle/list/<int:pk>', MotorcycleView.as_view(), name='v-motorcycle-view'),
    path('motorcycle/update/<int:pk>/', MotorcycleUpdateView.as_view(), name='v-motorcycle-update'),
    path('motorcycle/delete/<int:pk>/', MotorcycleDeleteView.as_view(), name='v-motorcycle-delete'),

    # cars
    
]