from django.urls import path
from . import views
from .views import ChatListView
from .views import ChatDetailView

urlpatterns = [
    # wildcard: we specify that the route can match /5 or /6
    path('<int:pk>/', ChatDetailView.as_view()),
    path('', ChatListView.as_view()),
]