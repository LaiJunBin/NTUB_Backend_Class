from django.shortcuts import render
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from .models import Commit, Post
from .permissions import CanUpdateOrDeleteCommit, IsCreatorOrReadOnly
from .serializers import CommitSerializer, PostSerializer


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsCreatorOrReadOnly]

    # def get_serializer_class(self):
    #     serializer = super().get_serializer_class()
    #     if self.request.method not in SAFE_METHODS:
    #         return CreatePostSerializer

    #     return serializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_serializer_class(self):
        serializer = super().get_serializer_class()
        if self.action == 'commit':
            return CommitSerializer

        if self.action == 'like':
            return Serializer

        return serializer

    @action(['PATCH'], True, permission_classes=[IsAuthenticated])
    def like(self, request, pk):
        post = self.get_object()
        if request.user in post.likes.all():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        serializer = self.get_serializer(post)
        return Response(serializer.data)

    @action(['POST'], True, permission_classes=[IsAuthenticated])
    def commit(self, request, pk):
        post = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(creator=self.request.user, post=post)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class CommitViewSet(viewsets.ReadOnlyModelViewSet, mixins.UpdateModelMixin, mixins.RetrieveModelMixin):
    queryset = Commit.objects.all()
    serializer_class = CommitSerializer
    permission_classes = [IsAuthenticated, CanUpdateOrDeleteCommit]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_serializer_class(self):
        serializer = super().get_serializer_class()

        if self.action == 'like':
            return LikesSerializer

        return serializer

    @action(['PATCH'], True, permission_classes=[IsAuthenticated])
    def like(self, request, pk):
        commit = self.get_object()
        if request.user in commit.likes.all():
            commit.likes.remove(request.user)
        else:
            commit.likes.add(request.user)

        serializer = self.get_serializer(commit)
        return Response(serializer.data)
