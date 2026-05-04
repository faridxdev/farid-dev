from django.db import migrations
from django.utils.text import slugify

def add_cv_projects(apps, schema_editor):
    Project = apps.get_model('projects', 'Project')
    Technology = apps.get_model('projects', 'Technology')

    # Projet 1 : KATAUPARFUM
    p1, _ = Project.objects.update_or_create(
        title="KATAUPARFUM",
        defaults={
            'category': 'web',
            'description_short': "Plateforme e-commerce complète avec gestion des produits et catégories, panier dynamique basé sur les sessions Django, système de commande et génération automatique de messages WhatsApp.",
            'description_full': (
                "Développement d'une plateforme e-commerce avec gestion des produits et catégories, "
                "ainsi qu'un panier dynamique basé sur les sessions. Mise en place d'un système de commande "
                "avec génération automatique de messages WhatsApp et déploiement sur Render."
            ),
            'architecture': "MVT Django",
            'database_info': "PostgreSQL",
            'icon': "🛍️",
            'is_featured': True,
            'order': 1,
            'slug': slugify("KATAUPARFUM"),
            'github_url': "https://github.com/faridxdev",
            'demo_url': "https://katauparfum.onrender.com"
        }
    )
    p1.technologies.add(*Technology.objects.filter(name__in=['Django', 'Python', 'PostgreSQL', 'Tailwind CSS', 'Render', 'JavaScript']))

    # Projet 2 : EduPlatform
    p2, _ = Project.objects.update_or_create(
        title="EduPlatform",
        defaults={
            'category': 'web',
            'description_short': "Plateforme de gestion des cours, tests en ligne et utilisateurs (admins, enseignants, étudiants). Conception BD, interfaces responsives, système de rôles et notation automatique.",
            'description_full': (
                "Développement d'une plateforme web de gestion des cours, tests et utilisateurs "
                "(administrateurs, enseignants, étudiants). Conception BD, interfaces responsives, "
                "rôles utilisateurs, et notation automatique."
            ),
            'architecture': "MVC Laravel",
            'database_info': "MySQL",
            'icon': "🎓",
            'is_featured': True,
            'order': 2,
            'slug': slugify("EduPlatform"),
            'github_url': "https://github.com/faridxdev"
        }
    )
    p2.technologies.add(*Technology.objects.filter(name__in=['Laravel', 'PHP', 'MySQL', 'Bootstrap', 'JavaScript']))

    # Projet 3 : Reconnaissance Faciale
    p3, _ = Project.objects.update_or_create(
        title="Présence par Reconnaissance Faciale",
        defaults={
            'category': 'api',
            'description_short': "Système automatisé de gestion des présences par reconnaissance faciale : enrôlement biométrique, pointage via webcam, gestion des utilisateurs par rôles, génération de rapports PDF/CSV et sécurisation des données faciales.",
            'description_full': (
                "Développement d'un système de gestion automatisée des présences étudiantes par reconnaissance "
                "faciale avec enrôlement biométrique, pointage via webcam et gestion des utilisateurs par rôles. "
                "Génération de rapports PDF/CSV et sécurisation des données faciales."
            ),
            'architecture': "MVT Django / IA",
            'database_info': "PostgreSQL",
            'icon': "🤖",
            'is_featured': True,
            'order': 3,
            'slug': slugify("Présence par Reconnaissance Faciale"),
            'github_url': "https://github.com/faridxdev"
        }
    )
    p3.technologies.add(*Technology.objects.filter(name__in=['Django', 'Python', 'OpenCV', 'DeepFace', 'PostgreSQL', 'JavaScript']))

    # Projet 4 : Système de Suivi des Patients - Clinique Perle du Nord
    p4, _ = Project.objects.update_or_create(
        title="Système de Suivi des Patients - Clinique Perle du Nord",
        defaults={
            'category': 'erp',
            'description_short': "Application web Django de gestion médicale interne. Gestion des patients, rendez-vous (FullCalendar) et dossiers médicaux dans une interface moderne et sécurisée.",
            'description_full': (
                "Application web Django de gestion médicale interne pour la Clinique Perle du Nord. "
                "Elle permet aux secrétaires de gérer les patients et rendez-vous, aux médecins d’enregistrer "
                "les consultations et dossiers médicaux, le tout dans une interface moderne (Tailwind/DaisyUI)."
            ),
            'architecture': "MVT Django",
            'database_info': "SQLite / PostgreSQL",
            'icon': "🏥",
            'is_featured': True,
            'order': 4,
            'slug': slugify("Suivi Patients Clinique Perle du Nord"),
            'github_url': "https://github.com/faridxdev"
        }
    )
    p4.technologies.add(*Technology.objects.filter(name__in=['Django', 'Python', 'PostgreSQL', 'Tailwind CSS', 'JavaScript']))

    # Projet 5 : Système de Gestion Scolaire (basé sur le design fourni)
    p5, _ = Project.objects.update_or_create(
        title="Système de Gestion Scolaire",
        defaults={
            'category': 'erp',
            'description_short': "Application complète de gestion scolaire : inscriptions, notes, emplois du temps, présences, bulletins PDF générés automatiquement et tableau de bord admin.",
            'description_full': (
                "Application complète de gestion scolaire : inscriptions, notes, emplois du temps, présences, "
                "bulletins PDF générés automatiquement et tableau de bord admin."
            ),
            'architecture': "Modules Django",
            'database_info': "PostgreSQL",
            'icon': "🏫",
            'is_featured': True,
            'order': 5,
            'slug': slugify("Système de Gestion Scolaire"),
            'github_url': "https://github.com/faridxdev"
        }
    )
    p5.technologies.add(*Technology.objects.filter(name__in=['Django', 'Python', 'PostgreSQL', 'Bootstrap', 'WeasyPrint']))

    # Projet 6 : PerteDocs.tg
    p6, _ = Project.objects.update_or_create(
        title="PerteDocs.tg",
        defaults={
            'category': 'web',
            'description_short': "Plateforme web de déclaration de perte de pièces administratives au Togo. Upload dynamique via HTMX, suivi de statut et génération de PDF officiels.",
            'description_full': (
                "Application moderne permettant aux citoyens togolais de déclarer en ligne la perte de documents "
                "(CNI, Passeport, Permis). Fonctionnalités : upload dynamique (HTMX), suivi de statut, "
                "dashboard admin puissant et génération automatique de PDF (style République Togolaise)."
            ),
            'architecture': "Django / HTMX / Docker",
            'database_info': "PostgreSQL",
            'icon': "🇹🇬",
            'is_featured': True,
            'order': 6,
            'slug': slugify("PerteDocs.tg"),
            'github_url': "https://github.com/faridxdev"
        }
    )
    p6.technologies.add(*Technology.objects.filter(name__in=['Django', 'Python', 'PostgreSQL', 'Bootstrap', 'WeasyPrint', 'Docker']))

class Migration(migrations.Migration):
    dependencies = [
        ('projects', '0002_initial_technologies'), # <-- Assurez-vous que c'est le nom du fichier généré
    ]
    operations = [
        migrations.RunPython(add_cv_projects),
    ]