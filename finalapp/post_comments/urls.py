from django.urls import path
from . import views

from .views import PostCommentsDetailView

urlpatterns = [
    path('<int:pk>/', PostCommentsDetailView.as_view()),
    path('', PostCommentsListView.as_view()),
]

from .views import PostCommentsListView