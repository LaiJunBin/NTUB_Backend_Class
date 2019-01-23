from rest_framework import serializers

from django.contrib.auth import get_user_model

from .models import Post, Commit

User = get_user_model()

class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class PostCommitSerializer(serializers.ModelSerializer):
    likes = LikesSerializer(many=True, read_only=True)

    class Meta:
        model = Commit
        fields = [
            'id',
            'content',
            'creator',
            'likes',
            'create_at',
            'update_at',
        ]


class PostSerializer(serializers.ModelSerializer):
    likes = LikesSerializer(many=True, read_only=True)
    commits = PostCommitSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = [
            'id',
            'creator',
            'create_at',
            'update_at',
        ]


class CommitSerializer(serializers.ModelSerializer):
    likes = LikesSerializer(many=True, read_only=True)

    class Meta:
        model = Commit
        fields = '__all__'
        read_only_fields = [
            'id',
            'post',
            'creator',
            'create_at',
            'update_at',
        ]
