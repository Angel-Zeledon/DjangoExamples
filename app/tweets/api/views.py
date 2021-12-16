from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from tweets.api.serializers import TweetModelSerializer
from tweets.models import Tweet

class TweetListAPIView(APIView):

    def get(self, request, pk ):
        tweet = Tweet.objects.get(id = pk)
        serializer = TweetModelSerializer(tweet)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def post(self, request, format = None):
        serializer = TweetModelSerializer(data = request.data)
        if serializer.is_valid(raise_exception = True):
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)    