from django.shortcuts import get_object_or_404
from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, required=False, slug_field='username')

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, required=False, slug_field='username')

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post', )


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True, required=False)
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all())

    def validate_following(self, value):
        user = self.context['request'].user
        following = get_object_or_404(User, username=value)

        if Follow.objects.filter(user=user, following=following).exists():
            raise serializers.ValidationError('Подписка уже существует!')

        if user == following:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!')
        return value

    class Meta:
        fields = ('user', 'following',)
        model = Follow
