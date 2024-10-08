from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from users.apps import UsersConfig
from users.views import UserCreateView, ProfileView, email_verification, recovery_password, UserListView, UserUpdateView, UserDeleteView, UserDetailView

app_name = UsersConfig.name


urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('users/<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('recovery/', recovery_password, name='recovery'),
    path('profile/', ProfileView.as_view(), name='profile'),
]