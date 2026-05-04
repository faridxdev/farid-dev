from django.db import migrations
from django.utils.text import slugify

def add_base_techs(apps, schema_editor):
    Technology = apps.get_model('projects', 'Technology')
    techs = [
        {'name': 'Python', 'color': '#3776ab'},
        {'name': 'Django', 'color': '#092e20'},
        {'name': 'PostgreSQL', 'color': '#336791'},
        {'name': 'Laravel', 'color': '#ff2d20'},
        {'name': 'Docker', 'color': '#2496ed'},
        {'name': 'OpenCV', 'color': '#5c3ee8'},
        {'name': 'JavaScript', 'color': '#f7df1e'},
        {'name': 'Bootstrap', 'color': '#7952b3'},
        {'name': 'Tailwind CSS', 'color': '#38b2ac'},
        {'name': 'WordPress', 'color': '#21759b'},
        {'name': 'DeepFace', 'color': '#ff4b4b'},
        {'name': 'JMerise', 'color': '#4a5568'},
        {'name': 'Render', 'color': '#22C55E'},
        {'name': 'Django REST', 'color': '#092e20'},
        {'name': 'JWT Auth', 'color': '#000000'},
        {'name': 'Swagger', 'color': '#85ea2d'},
        {'name': 'WeasyPrint', 'color': '#1e1e1e'},
        {'name': 'REST API', 'color': '#000000'},
    ]
    for tech in techs:
        Technology.objects.update_or_create(
            name=tech['name'],
            defaults={'color': tech['color'], 'slug': slugify(tech['name'])}
        )

class Migration(migrations.Migration):
    dependencies = [
        ('projects', '0001_initial'), # <-- Assurez-vous que c'est le nom du fichier généré
    ]
    operations = [
        migrations.RunPython(add_base_techs),
    ]