from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin
from .models import Post, User, Comment


@admin.register(Post)
class SortablePostAdmin(SortableAdminMixin, admin.ModelAdmin):
    ordering = []
    list_display = ['caption', 'photo', 'tags', 'datetime']


@admin.register(User)
class SortableUserAdmin(SortableAdminMixin, admin.ModelAdmin):
    ordering = []
    list_display = ['username', 'email', 'phone_number', 'is_owner', 'is_active', 'date_joined']


@admin.register(Comment)
class SortableCommentAdmin(SortableAdminMixin, admin.ModelAdmin):
    ordering = []
    list_display = ['text', 'datetime', 'user', 'post', 'is_reply_to']
