from django.db import models
from django.utils.text import slugify

class Technology(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)
    color = models.CharField(max_length=10, default="#3b82f6")

    class Meta:
        verbose_name = "Technologie"
        verbose_name_plural = "Technologies"

    def save(self, *args, **kwargs):
        if not self.slug:
            original_slug = slugify(self.name)
            count = Technology.objects.filter(slug__iexact=original_slug).count()
            if count > 0:
                self.slug = f"{original_slug}-{count}"
            else:
                self.slug = original_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Application Web'),
        ('api', 'API Backend'),
        ('desktop', 'Application Desktop'),
        ('mobile', 'Application Mobile'),
        ('erp', 'ERP / Gestion'),
        ('other', 'Autre'),
    ]
    STATUS_CHOICES = [
        ('completed', 'Terminé'),
        ('in_progress', 'En cours'),
        ('maintenance', 'Maintenance'),
    ]

    title = models.CharField("Titre", max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField("Catégorie", max_length=20, choices=CATEGORY_CHOICES)
    status = models.CharField("Statut", max_length=20, choices=STATUS_CHOICES, default='completed')
    description_short = models.CharField("Description courte", max_length=300)
    description_full = models.TextField("Description complète")
    architecture = models.CharField("Architecture", max_length=200, blank=True)
    database_info = models.CharField("Base de données", max_length=100, blank=True)
    features = models.TextField("Fonctionnalités backend (une par ligne)", blank=True)
    technologies = models.ManyToManyField(Technology, related_name='projects')
    thumbnail = models.ImageField("Miniature", upload_to='projects/thumbnails/', blank=True)
    github_url = models.URLField("GitHub", blank=True)
    demo_url = models.URLField("Démo", blank=True)
    icon = models.CharField("Icône (emoji)", max_length=10, default="🔧")
    is_featured = models.BooleanField("Mis en avant", default=False)
    order = models.PositiveIntegerField("Ordre", default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Projet"

    def save(self, *args, **kwargs):
        if not self.slug:
            original_slug = slugify(self.title)
            queryset = Project.objects.filter(slug__iexact=original_slug).count()
            if queryset > 0:
                self.slug = f"{original_slug}-{queryset}"
            else:
                self.slug = original_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_features_list(self):
        return [f.strip() for f in self.features.split('\n') if f.strip()]


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='projects/screenshots/')
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Image du projet"
        verbose_name_plural = "Images du projet"