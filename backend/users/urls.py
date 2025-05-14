from django.urls import path
from .views import CurrentUserView, UserListView, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView, TokenObtainPair

urlpatterns = [
    path('users/current/', CurrentUserView.as_view(), name='user-current'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
    path('users/login/', TokenObtainPair.as_view(), name='token_obtain_pair'),
]