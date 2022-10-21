from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User as AdminUser


class Post(models.Model):
    photo = models.ImageField(
        verbose_name=_('photo'),
    )

    caption = models.CharField(
        verbose_name=_('caption'),
        max_length=150,
        blank=True,
        unique=False,
    )

    tags = models.CharField(
        verbose_name=_('tags'),
        max_length=150,
        blank=True,
        unique=False,
    )

    datetime = models.DateTimeField(
        verbose_name=_('last update date and time'),
        auto_now=True,
    )

    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        ordering = ['order']

    def __str__(self):
        return self.caption


class User(AdminUser):
    phone_number = models.CharField(
        verbose_name=_('phone number'),
        max_length=13,
        blank=True,
        unique=True,
    )

    is_owner = models.BooleanField(
        verbose_name=_('admin status'),
        default=False,
    )

    favourite_posts = models.ManyToManyField(
        Post,
        verbose_name=_('favourite posts'),
        blank=True,
        default=None,
    )

    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta(AdminUser.Meta):
        ordering = ['order']

    def __str__(self):
        return self.username


class Comment(models.Model):
    text = models.CharField(
        verbose_name=_('comment text'),
        max_length=256,
    )

    datetime = models.DateTimeField(
        verbose_name=_('last update date and time'),
        auto_now=True,
    )

    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name=_('user that left the comment')
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name=_('post that the comment is related to'),
    )

    is_reply_to = models.ForeignKey(
        'self',
        on_delete=models.DO_NOTHING,
        verbose_name=_('this comment is a reply to a comment...'),
        blank=True,
        null=True,
    )

    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comment')
        ordering = ['order']

    def __str__(self):
        return self.text
