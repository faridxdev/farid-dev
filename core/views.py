from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from projects.models import Project, Technology
from .models import SiteSettings, Skill, Education, Experience, Certification
from contact.forms import ContactForm

def home_view(request):
    # Logique de traitement du formulaire de contact
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            
            # Envoi d'une notification par email à vous-même
            send_mail(
                subject=f"Nouveau message Portfolio: {contact.subject}",
                message=f"De: {contact.name} ({contact.email})\n\nMessage:\n{contact.message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=True, # Évite de faire planter le site si l'envoi d'email échoue
            )

            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({
                    'status': 'success',
                    'message': "Votre message a été envoyé avec succès ! Je vous répondrai très prochainement."
                })

            messages.success(request, "Votre message a été envoyé avec succès ! Je vous répondrai très prochainement.")
            return redirect('/#contact')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                # Transforme les erreurs en un message lisible
                error_messages = []
                for field, errors in form.errors.items():
                    field_name = field.capitalize() if field != '__all__' else "Erreur"
                    error_messages.append(f"{field_name}: {', '.join(errors)}")
                return JsonResponse({'status': 'error', 'message': " | ".join(error_messages)}, status=400)

    else:
        form = ContactForm()

    settings_obj = SiteSettings.objects.first() or SiteSettings(name="Votre Nom", title="Développeur")
    featured_projects = Project.objects.filter(is_featured=True)[:6]
    featured_skills = Skill.objects.filter(is_featured=True).order_by('order')
    all_technologies = Technology.objects.all().order_by('name') # Pour la section "Toutes les technologies"

    # Organisation des compétences par groupes pour le template
    skills_groups = {
        'priority': featured_skills.filter(name__in=['Python', 'Django', 'Django REST Framework', 'OpenCV / DeepFace']),
        'php_laravel': featured_skills.filter(name__in=['PHP', 'Laravel']),
        'java': featured_skills.filter(name__in=['Java', 'Java / Java Swing']),
        'database': featured_skills.filter(category='database'),
        'frontend_tools': featured_skills.filter(category__in=['frontend', 'devops']),
    }

    context = {
        'site': settings_obj,
        'featured_projects': featured_projects,
        'skills': featured_skills,
        'skills_groups': skills_groups,
        'all_technologies': all_technologies,
        'experiences': Experience.objects.all(),
        'educations': Education.objects.all(),
        'certifications': Certification.objects.all(),
        'contact_form': form,
    }
    return render(request, 'core/home.html', context)