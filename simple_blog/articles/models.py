from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class Article(models.Model):
    title = models.CharField(_('タイトル'), max_length=100)
    description = models.TextField(_('内容'), max_length=1000, blank=True)
    created_at = models.DateTimeField(_('作成日時'), auto_now_add=True)
    updated_at = models.DateTimeField(_('更新日時'), auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('articles:detail', args=[str(self.id)])
