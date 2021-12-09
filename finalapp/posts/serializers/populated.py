from post_comments.serializers.common import PostCommentsSerializer
from .common import PostSerializer


class PopulatedPostSerializer(PostSerializer):
    post_comments = PostCommentsSerializer(many=True)