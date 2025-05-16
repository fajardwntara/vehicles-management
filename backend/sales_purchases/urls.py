from django.urls import path
from .views import (
    SaleCreateView, SaleUpdateView, SaleListView,
    PurchaseCreateView, PurchaseUpdateView, PurchaseListView,
    TotalTransactionView
)

urlpatterns = [
    # sales
    path('sales/lists/', SaleListView.as_view(), name='sale-lists'),
    path('sales/create/', SaleCreateView.as_view(), name='sale-create'),
    path('sales/update/<int:pk>/', SaleUpdateView.as_view(), name='sale-cancel'),

    # purchases
    path('purchases/lists/', PurchaseListView.as_view(), name='purchase-lists'),
    path('purchases/create/', PurchaseCreateView.as_view(), name='purchase-create'),
    path('purchases/update/<int:pk>/', PurchaseUpdateView.as_view(), name='purchase-cancel'),

    # transaction report
    path('transaction/total-transaction/', TotalTransactionView.as_view(), name='total-transaction'),
]