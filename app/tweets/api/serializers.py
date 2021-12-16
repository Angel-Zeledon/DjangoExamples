from rest_framework.serializers import ModelSerializer
from tweets.models import Tweet
from login.models import Usuario

class TweetModelSerializer(ModelSerializer):
    Usuario()
    class Meta:
        model = Tweet
        fields = [
            'id',
            'title',
            'description',
            'created_at',
            'author'
        ]

