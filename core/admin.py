from django.contrib import admin
from django.utils.html import format_html
from .models import SiteSettings, Skill, Education, Experience, Certification

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Identité', {'fields': ('name', 'title', 'tagline', 'avatar', 'favicon', 'is_available')}),
        ('Biographie', {'fields': ('bio_short', 'bio_long')}),
        ('Contact & Réseaux', {'fields': ('email', 'phone', 'whatsapp', 'github', 'linkedin', 'twitter')}),
        ('Fichiers', {'fields': ('cv_file',)}),
        ('Statistiques', {'fields': ('years_experience', 'projects_count', 'technologies_count')}),
    )

    def has_add_permission(self, request):
        # Un seul objet autorisé
        return not SiteSettings.objects.exists()


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'percentage_bar', 'is_featured', 'order']
    list_filter = ['category', 'is_featured']
    list_editable = ['is_featured', 'order']
    ordering = ['order']

    def percentage_bar(self, obj):
        color = '#3b82f6' if obj.percentage >= 70 else '#f59e0b'
        return format_html(
            '<div style="width:120px;background:#1e3a5f;border-radius:4px;height:8px;">'
            '<div style="width:{}%;background:{};height:8px;border-radius:4px;"></div>'
            '</div> {}%',
            obj.percentage, color, obj.percentage
        )
    percentage_bar.short_description = "Niveau"


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_year', 'end_year', 'is_current']
    list_editable = ['is_current']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'organization', 'start_date', 'is_current']

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'issuer', 'date']