from django.urls import path
from .views import CurrentUserView, UserListView, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView, TokenObtainPair

urlpatterns = [
    path('current/', CurrentUserView.as_view(), name='user-current'),
    path('', UserListView.as_view(), name='user-list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('create/', UserCreateView.as_view(), name='user-create'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user-update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
    path('login/', TokenObtainPair.as_view(), name='token_obtain_pair'),
]