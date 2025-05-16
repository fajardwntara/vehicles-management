from django.urls import path
from .views import (
    SaleCreateView, SaleUpdateView, SaleListView, SaleDeleteAPIView,
    PurchaseCreateView, PurchaseUpdateView, PurchaseListView, PurchaseDeleteAPIView,
    TotalTransactionView
)

urlpatterns = [
    # sales
    path('sales/lists/', SaleListView.as_view(), name='sale-lists'),
    path('sales/create/', SaleCreateView.as_view(), name='sale-create'),
    path('sales/update/<int:pk>/', SaleUpdateView.as_view(), name='sale-cancel'),
    path('sales/delete/<int:pk>/', SaleDeleteAPIView.as_view(), name='sale-delete'),

    # purchases
    path('purchases/lists/', PurchaseListView.as_view(), name='purchase-lists'),
    path('purchases/create/', PurchaseCreateView.as_view(), name='purchase-create'),
    path('purchases/update/<int:pk>/', PurchaseUpdateView.as_view(), name='purchase-cancel'),
    path('purchases/delete/<int:pk>/', PurchaseDeleteAPIView.as_view(), name='purchase-delete'),

    # transaction report
    path('transaction/total-transaction/', TotalTransactionView.as_view(), name='total-transaction'),
]