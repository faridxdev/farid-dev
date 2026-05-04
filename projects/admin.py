from django.contrib import admin
from .models import Project, Technology, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'is_featured', 'order', 'created_at')
    list_filter = ('category', 'status', 'is_featured', 'technologies')
    search_fields = ('title', 'description_short', 'description_full')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline]
    filter_horizontal = ('technologies',)

@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    prepopulated_fields = {'slug': ('name',)}