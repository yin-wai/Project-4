from django.http.response import HttpResponse
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  # status code

from .models import Chats
from .serializers.common import ChatSerializer
from .serializers.populated import PopulatedChatSerializer


class ChatDetailView(APIView):
    def delete(self, request, pk):
        try:
            chat_status = Chats.objects.get(id=pk)
            chat_status.delete()
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        chat_status = Chats.objects.get(id=pk)  # django ORM method to grab
        updated_chat = ChatSerializer(chat_status, data=request.data)
        if updated_chat.is_valid():
            updated_chat.save()
            return Response(updated_chat.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(updated_chat.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def get(self, _request, pk):
        chat_status = Chats.objects.get(id=pk)
        serialized_Chat = PopulatedChatSerializer(chat_status)
        return Response(serialized_Chat.data, status=status.HTTP_200_OK)


class ChatListView(APIView):
    # will kick in if someone tries to Chat
    def Chat(self, request):
        request.data["author"] = request.user.id
        chat_status = ChatSerializer(data=request.data)
        if chat_status.is_valid():
            chat_status.save()  # <--- django ORM method to save to db
            return Response(chat_status.data, status=status.HTTP_201_CREATED)
        else:
            return Response(chat_status.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def get(self, request):
        chats = Chats.objects.all()
        serialized_chats = PopulatedChatSerializer(chats, many=True)
        return Response(serialized_chats.data, status=status.HTTP_200_OK)