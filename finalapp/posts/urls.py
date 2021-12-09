from django.urls import path
from . import views
from .views import PostDetailView
from .views import PostListView
# from post_reply. import PostReply
urlpatterns = [
    # wildcard: we specify that the route can match /5 or /6
    path('<int:pk>/', PostDetailView.as_view()),
    path('', PostListView.as_view()),
]