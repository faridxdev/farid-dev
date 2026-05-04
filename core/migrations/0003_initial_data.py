from django.db import migrations

def create_initial_data(apps, schema_editor):
    SiteSettings = apps.get_model('core', 'SiteSettings')
    Education = apps.get_model('core', 'Education')
    Skill = apps.get_model('core', 'Skill')

    # 1. Paramètres globaux
    SiteSettings.objects.update_or_create(
        id=1,
        defaults={
            'name': 'AGBOKA FARID',
            'title': 'Développeur Backend',
            'tagline': "Développeur backend passionné par Python et Django, spécialisé en conception d'APIs robustes, architecture logicielle et bases de données relationnelles. Je construis des solutions fiables et orientées métier.",
            'bio_short': "développeur backend de 20 ans basé à Lomé, Togo.",
            'bio_long': "Je m'appelle AGBOKA FARID, développeur backend de 20 ans basé à Lomé, Togo. Python est mon langage de prédilection — je l'utilise au quotidien avec Django pour concevoir des applications web robustes, des APIs REST et des systèmes intelligents comme la reconnaissance faciale.\n\nPassionné par l'architecture logicielle, la logique métier et la conception de bases de données, je maîtrise également Laravel, Java et les bases relationnelles PostgreSQL/MySQL. J'aime transformer des idées complexes en solutions backend propres et maintenables.",
            'email': 'agbokafarid@gmail.com',
            'phone': '+228 91 13 51 72',
            'location': 'Zossimé, Lomé — Togo',
            'whatsapp': '22891135172',
            'github': 'https://github.com/faridxdev',
            'linkedin': 'https://linkedin.com/in/agbokafarid',
            'is_available': True,
            'projects_count': 6,
            'technologies_count': 14,
            'years_experience': 2,
        }
    )

    # 2. Formations (Education)
    Education.objects.update_or_create(
        degree="Licence en informatique : Développement d'Applications",
        institution="Institut FORMATEC",
        defaults={
            'location': 'Lomé, Togo',
            'start_year': 2023,
            'is_current': True,
            'description': "Spécialisation backend, bases de données, algorithmique et conception logicielle.",
            'order': 1
        }
    )
    Education.objects.update_or_create(
        degree="Baccalauréat — Mention Assez-Bien",
        institution="CS SAVOIR KOHE",
        defaults={
            'location': 'Lomé, Togo',
            'start_year': 2022,
            'end_year': 2023,
            'description': "Mention assez-bien. Initiation à l'informatique et aux mathématiques.",
            'order': 2
        }
    )

    # 3. Compétences (Skills)
    skills_data = [
        # name, category, percentage, order, color
        ('Python', 'backend', 88, 1, 'linear-gradient(90deg,var(--python),var(--python2))'),
        ('Django', 'backend', 85, 2, 'linear-gradient(90deg,var(--python),var(--python2))'),
        ('Django REST Framework', 'backend', 80, 3, 'linear-gradient(90deg,var(--python),var(--python2))'),
        ('OpenCV / DeepFace', 'backend', 72, 4, 'linear-gradient(90deg,var(--python),var(--python2))'),
        ('Laravel', 'backend', 80, 5, '#f59e0b'),
        ('PHP', 'backend', 75, 6, '#f59e0b'),
        ('Java / Java Swing', 'backend', 70, 7, '#ef4444'),
        ('PostgreSQL', 'database', 82, 8, '#3b82f6'),
        ('MySQL', 'database', 82, 9, '#3b82f6'),
        ('SQLite', 'database', 75, 10, '#3b82f6'),
        ('JMerise / Modélisation', 'database', 78, 11, '#3b82f6'),
        ('HTML / CSS / Bootstrap', 'frontend', 78, 12, '#8b5cf6'),
        ('Tailwind CSS', 'frontend', 74, 13, '#8b5cf6'),
        ('JavaScript', 'frontend', 65, 14, '#8b5cf6'),
        ('Git / GitHub', 'devops', 78, 15, '#6366f1'),
    ]

    for name, cat, pct, order, color in skills_data:
        Skill.objects.update_or_create(
            name=name,
            defaults={
                'category': cat,
                'percentage': pct,
                'order': order,
                'color': color,
                'is_featured': True
            }
        )

class Migration(migrations.Migration):
    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_data),
    ]