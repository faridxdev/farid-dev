from django.contrib import admin
from .models import Article, Tag

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_published', 'is_featured', 'views_count', 'created_at']
    list_filter = ['is_published', 'is_featured', 'tags']
    list_editable = ['is_published', 'is_featured']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['tags']
    readonly_fields = ['views_count', 'created_at', 'updated_at']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'color']
    prepopulated_fields = {'slug': ('name',)}