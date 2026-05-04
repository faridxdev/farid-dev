from django.db import models

class SiteSettings(models.Model):
    """Paramètres globaux du portfolio (singleton)"""
    name = models.CharField("Nom complet", max_length=100)
    title = models.CharField("Titre professionnel", max_length=200)
    tagline = models.CharField("Accroche", max_length=300)
    bio_short = models.TextField("Bio courte")
    bio_long = models.TextField("Bio complète")
    avatar = models.ImageField("Photo", upload_to='avatar/', blank=True)
    favicon = models.ImageField("Favicon", upload_to='settings/', blank=True, help_text="Format ICO ou PNG (32x32)")
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField("Localisation", max_length=200, blank=True)
    whatsapp = models.CharField(max_length=20, blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    cv_file = models.FileField("CV (PDF)", upload_to='cv/', blank=True)
    is_available = models.BooleanField("Disponible", default=True)
    years_experience = models.PositiveIntegerField(default=2)
    projects_count = models.PositiveIntegerField(default=10)
    technologies_count = models.PositiveIntegerField(default=15)

    class Meta:
        verbose_name = "Paramètres du site"

    def __str__(self):
        return f"Portfolio de {self.name}"


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('backend', 'Backend'),
        ('database', 'Base de données'),
        ('frontend', 'Frontend'),
        ('devops', 'DevOps / Outils'),
        ('other', 'Autre'),
    ]
    name = models.CharField("Technologie", max_length=100)
    category = models.CharField("Catégorie", max_length=20, choices=CATEGORY_CHOICES)
    percentage = models.PositiveIntegerField("Niveau (%)", default=70)
    icon = models.CharField("Icône (emoji/class)", max_length=50, blank=True)
    color = models.CharField("Couleur hex", max_length=255, default="#3b82f6")
    order = models.PositiveIntegerField("Ordre", default=0)
    is_featured = models.BooleanField("Mis en avant", default=False)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Compétence"
        verbose_name_plural = "Compétences"

    def __str__(self):
        return f"{self.name} — {self.percentage}%"


class Education(models.Model):
    degree = models.CharField("Diplôme", max_length=200)
    institution = models.CharField("Établissement", max_length=200)
    location = models.CharField("Lieu", max_length=100)
    start_year = models.PositiveIntegerField("Année début")
    end_year = models.PositiveIntegerField("Année fin", null=True, blank=True)
    is_current = models.BooleanField("En cours", default=False)
    description = models.TextField("Description", blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-start_year']
        verbose_name = "Formation"
        verbose_name_plural = "Formations"

    def __str__(self):
        return f"{self.degree} — {self.institution}"


class Experience(models.Model):
    title = models.CharField("Poste / Titre", max_length=200)
    organization = models.CharField("Organisation", max_length=200)
    start_date = models.DateField("Date début")
    end_date = models.DateField("Date fin", null=True, blank=True)
    is_current = models.BooleanField("En cours", default=False)
    description = models.TextField("Description")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-start_date']
        verbose_name = "Expérience"
        verbose_name_plural = "Expériences"

    def __str__(self):
        return f"{self.title} chez {self.organization}"


class Certification(models.Model):
    name = models.CharField("Nom", max_length=200)
    issuer = models.CharField("Organisme", max_length=100)
    date = models.DateField("Date d'obtention", null=True, blank=True)
    url = models.URLField("Lien certificat", blank=True)
    icon = models.CharField("Icône", max_length=10, default="🏆")

    class Meta:
        ordering = ['-date']
        verbose_name = "Certification"

    def __str__(self):
        return f"{self.name} — {self.issuer}"