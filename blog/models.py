from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Tag(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, blank=True)
    color = models.CharField(max_length=10, default="#3b82f6")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField("Titre", max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    excerpt = models.TextField("Extrait", max_length=400)
    content = RichTextField("Contenu")
    tags = models.ManyToManyField(Tag, related_name='articles', blank=True)
    thumbnail = models.ImageField("Image", upload_to='blog/', blank=True)
    icon = models.CharField("Icône", max_length=10, default="📝")
    read_time = models.PositiveIntegerField("Temps de lecture (min)", default=5)
    is_published = models.BooleanField("Publié", default=False)
    is_featured = models.BooleanField("Mis en avant", default=False)
    views_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-published_at', '-created_at']
        verbose_name = "Article"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def increment_views(self):
        self.views_count += 1
        self.save(update_fields=['views_count'])