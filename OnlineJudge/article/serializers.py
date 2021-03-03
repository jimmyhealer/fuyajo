from utils.api import serializers
from utils.api._serializers import UsernameSerializer

from .models import Article


class CreateArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=64)
    content = serializers.CharField(max_length=1024 * 1024 * 8)
    visible = serializers.BooleanField()


class ArticleSerializer(serializers.ModelSerializer):
    created_by = UsernameSerializer()

    class Meta:
        model = Article
        fields = "__all__"


class EditArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=64)
    content = serializers.CharField(max_length=1024 * 1024 * 8)
    visible = serializers.BooleanField()
