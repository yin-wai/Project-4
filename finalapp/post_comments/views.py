from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import PostComments
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  # status code
from .serializers.common import PostCommentsSerializer


class PostCommentsDetailView(APIView):
    def delete(self, _request, pk):
        try:
            post_comments = PostComments.objects.get(id=pk)
            post_comments.delete()
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        post_comments = PostComments.objects.get(id=pk)  # django ORM method to grab
        updated_post_comments = PostCommentsSerializer(post_comments, data=request.data)
        if updated_post_comments.is_valid():
            updated_post_comments.save()
            return Response(updated_post_comments.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(updated_post_comments.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def get(self, _request, pk):
        post_comments = PostComments.objects.get(id=pk)
        serialized_post_comments = PostCommentsSerializer(post_comments)
        return Response(serialized_post_comments.data, status=status.HTTP_200_OK)


class PostCommentsListView(APIView):
    def post(self, request):
        request.data["author"] = request.user.id
        post_comments = PostCommentsSerializer(data=request.data)
        if post_comments.is_valid():
            post_comments.save()  # <--- django ORM method to save to db
            return Response(post_comments.data, status=status.HTTP_201_CREATED)
        else:
            return Response(post_comments.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def get(self, _request):
        posts_comments = PostComments.objects.all()
        serialized_posts_reply = PostCommentsSerializer(posts_comments, many=True)
        return Response(serialized_posts_reply.data, status=status.HTTP_200_OK)