from django.urls import path
from . import views
from .views import MessageListView
from .views import MessageDetailView, MessageBetweenUsersListView, MessageBetweenSentToUsersListView, MessageReceivedList, MessageSentListBetweenUser, SendMessageView
urlpatterns = [
    path('detail/<int:pk>/', MessageDetailView.as_view()),
    path('', MessageListView.as_view()),
    path('received/<int:author>/',
         MessageBetweenUsersListView.as_view()),
    path('received/<int:author>/<int:sent_to>/',
         MessageBetweenSentToUsersListView.as_view()),
    path('sent/<int:sent_to>/', MessageReceivedList.as_view()),
    path('sent/<int:sent_to>/<int:author>/',
         MessageSentListBetweenUser.as_view()),
    path('send_message/<int:pk>/', SendMessageView.as_view())
]