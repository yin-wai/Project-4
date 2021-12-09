from message_details.serializers.common import MessagesSerializer
from .common import ChatSerializer


class PopulatedChatSerializer(ChatSerializer):
    message_details = MessagesSerializer(many=True)