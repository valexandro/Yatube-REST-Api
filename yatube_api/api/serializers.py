from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


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
    user = serializers.SlugRelatedField(
        slug_field='username', read_only=True, required=False,
        default=serializers.CurrentUserDefault())
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all())

    class Meta:
        fields = ('user', 'following',)
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following', ],
                message='Подписка уже существует!',
            )
        ]

    def validate(self, data):
        if self.context['request'].user == data.get('following'):
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!')
        return data
