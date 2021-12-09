from rest_framework import serializers
from ..models import PostComments


class PostCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComments
        fields = '__all__'

        def __str__(self):
            return self