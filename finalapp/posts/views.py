from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  # status code
from .models import Post
from .serializers.common import PostSerializer
from .serializers.populated import PopulatedPostSerializer
class PostDetailView(APIView):
    def delete(self, request, pk):
        try:
            post_status = Post.objects.get(id=pk)
            post_status.delete()
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self, request, pk):
        post_status = Post.objects.get(id=pk)  # django ORM method to grab
        updated_post = PostSerializer(post_status, data=request.data)
        if updated_post.is_valid():
            updated_post.save()
            return Response(updated_post.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(updated_post.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    def get(self, _request, pk):
        post_status = Post.objects.get(id=pk)
        serialized_post = PopulatedPostSerializer(post_status)
        return Response(serialized_post.data, status=status.HTTP_200_OK)
class PostListView(APIView):
    def post(self, request):
        request.data["author"] = request.user.id
        post_status = PostSerializer(data=request.data)
        if post_status.is_valid():
            post_status.save()  # <--- django ORM method to save to db
            return Response(post_status.data, status=status.HTTP_201_CREATED)
        else:
            return Response(post_status.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    def get(self, request):
        posts = Post.objects.all()
        serialized_posts = PopulatedPostSerializer(posts, many=True)
        return Response(serialized_posts.data, status=status.HTTP_200_OK)