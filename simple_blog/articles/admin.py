from django.contrib import admin
from .models import Article

# Register your models here.


@admin.register(Article)
class LessonCourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
