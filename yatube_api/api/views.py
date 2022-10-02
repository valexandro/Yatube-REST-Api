from django.shortcuts import get_object_or_404
from posts.models import Group, Post
from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from .permissions import IsOwnerOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly, )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        return serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsOwnerOrReadOnly, )

    def get_post(self) -> Post:
        """Получает пост из параметров URL."""
        post_id: int = self.kwargs['post_id']
        return get_object_or_404(Post, id=post_id)

    def get_queryset(self):
        return self.get_post().comments

    def perform_create(self, serializer):
        return serializer.save(
            author=self.request.user,
            post=self.get_post()
        )


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('user__username', 'following__username',)
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return self.request.user.follower

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
