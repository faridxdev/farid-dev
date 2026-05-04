from django.db import models

class ContactMessage(models.Model):
    STATUS_CHOICES = [
        ('new', 'Nouveau'),
        ('read', 'Lu'),
        ('replied', 'Répondu'),
        ('archived', 'Archivé'),
    ]
    SUBJECT_CHOICES = [
        ('freelance', 'Projet Freelance'),
        ('job', 'Stage / Emploi'),
        ('collab', 'Collaboration'),
        ('other', 'Autre'),
    ]
    BUDGET_CHOICES = [
        ('negotiable', 'À définir'),
        ('less_300k', 'Moins de 300 000 FCFA'),
        ('300k_1m', '300 000 FCFA — 1 000 000 FCFA'),
        ('more_1m', 'Plus de 1 000 000 FCFA'),
    ]

    name = models.CharField("Nom", max_length=100)
    email = models.EmailField("Email")
    subject = models.CharField("Sujet", max_length=20, choices=SUBJECT_CHOICES)
    budget = models.CharField("Budget", max_length=50, choices=BUDGET_CHOICES, blank=True)
    message = models.TextField("Message")
    status = models.CharField("Statut", max_length=10, choices=STATUS_CHOICES, default='new')
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Message de contact"
        verbose_name_plural = "Messages de contact"

    def __str__(self):
        return f"{self.name} — {self.get_subject_display()} ({self.created_at.strftime('%d/%m/%Y')})"