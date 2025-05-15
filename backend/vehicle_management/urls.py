from django.urls import path
from .views import MotorcycleView, MotorcycleListView, MotorcycleCreateView

urlpatterns = [
    path('motorcycle/lists', MotorcycleListView.as_view(), name='v-motorcycle-lists'),
    path('motorcycle/create', MotorcycleCreateView.as_view(), name='v-motorcycle-create'),
]