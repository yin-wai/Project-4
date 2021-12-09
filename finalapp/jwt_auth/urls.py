from django.urls import path
from .views import RegisterView, LoginView,  UsersListView, UserDetailListView
urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('<int:pk>/', UserDetailListView.as_view()),
    path('', UsersListView.as_view())
]