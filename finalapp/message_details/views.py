from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Message
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status  # status code
from .serializers.common import MessagesSerializer
from jwt_auth.models import User
from rest_framework.permissions import IsAuthenticated
class MessageDetailView(APIView):
    def delete(self, _request, pk):
        try:
            message = Message.objects.get(id=pk)
            message.delete()
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self, request, pk):
        message = Message.objects.get(id=pk)  # django ORM method to grab
        updated_message = MessagesSerializer(message, data=request.data)
        if updated_message.is_valid():
            updated_message.save()
            return Response(updated_message.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(updated_message.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    def get(self, _request, pk):
        message = Message.objects.get(id=pk)
        serialized_message = MessagesSerializer(message)
        return Response(serialized_message.data, status=status.HTTP_200_OK)
class MessageListView(APIView):
    def get(self, request):
        print(request.data)
        message = Message.objects.all()
        serialized_message = MessagesSerializer(message, many=True)
        return Response(serialized_message.data, status=status.HTTP_200_OK)
class MessageBetweenUsersListView(APIView):
    def get(self, request, author):
        message = Message.objects.filter(author=author)
        serialized_message = MessagesSerializer(message, many=True)
        return Response(serialized_message.data, status=status.HTTP_200_OK)
class MessageBetweenSentToUsersListView(APIView):
    def get(self, request, author, sent_to):
        message = Message.objects.filter(author=author, sent_to=sent_to)
        serialized_message = MessagesSerializer(message, many=True)
        return Response(serialized_message.data, status=status.HTTP_200_OK)
class MessageReceivedList(APIView):
    def get(self, request, sent_to):
        message = Message.objects.filter(sent_to=sent_to)
        serialized_message = MessagesSerializer(message, many=True)
        return Response(serialized_message.data, status=status.HTTP_200_OK)
class MessageSentListBetweenUser(APIView):
    def get(self, request, author, sent_to):
        message = Message.objects.filter(author=author, sent_to=sent_to)
        serialized_message = MessagesSerializer(message, many=True)
        return Response(serialized_message.data, status=status.HTTP_200_OK)
class SendMessageView(APIView):
    def post(self, request, pk):
        permission_classes = (IsAuthenticated,)
        request.data["author"] = request.user.id
        print(request.data)
        request.data["sent_to"] = pk
        message = MessagesSerializer(data=request.data)
        if message.is_valid():
            message.save()  # <--- django ORM method to save to db
            return Response(message.data, status=status.HTTP_201_CREATED)
        else:
            return Response(message.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)