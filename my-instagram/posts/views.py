from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework import mixins
from rest_framework.serializers import Serializer

from .models import Post, Commit
from .permissions import IsCreatorOrReadOnly, CanSeePost
from .serializers import PostSerializer, CommitSerializer
from .mixins import CanLikeMixin

class PostViewSet(CanLikeMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsCreatorOrReadOnly, ]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_serializer_class(self):
        serializer = super().get_serializer_class()
        if self.action == 'commit':
            return CommitSerializer

        if self.action == 'like':
            return Serializer

        return serializer

    def get_permissions(self):
        permission = super().get_permissions()

        if self.action == 'retrieve':
            permission.append(CanSeePost())

        return permission

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.action == 'list':
            following_users = self.request.user.following.filter(is_agree=True).values_list('to_user', flat=True)
            queryset = queryset.filter(
                creator_id__in=following_users
            )

        return queryset

    @action(['POST'], True, permission_classes=[IsAuthenticated])
    def commit(self, request, pk):
        post = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(creator=self.request.user, post=post)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CommitViewSet(CanLikeMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.ReadOnlyModelViewSet):
    queryset = Commit.objects.all()
    serializer_class = CommitSerializer
    permission_classes = [IsAuthenticated, IsCreatorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_serializer_class(self):
        serializer = super().get_serializer_class()

        if self.action == 'like':
            return Serializer

        return serializer
