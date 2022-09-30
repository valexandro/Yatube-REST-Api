from django.contrib import admin

from .models import Comment, Follow, Group, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Настройка отображения постов в админке."""

    list_display = ('pk', 'text', 'pub_date', 'author', 'group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'
    list_editable = ('group',)


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    """Настройка отображения групп в админке."""

    list_display = ('title', 'slug',)
    empty_value_display = '-пусто-'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Настройка отображения комментариев в админке."""

    list_display = ('text', 'author', 'created',)
    empty_value_display = '-пусто-'


@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):

    list_display = ('user', 'following',)
    empty_value_display = '-пусто-'
