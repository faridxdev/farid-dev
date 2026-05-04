from .models import SiteSettings

def global_context(request):
    """Rend les infos globales disponibles dans tous les templates"""
    settings_obj = SiteSettings.objects.first()
    return {
        'site': settings_obj,
        'nav_links': [
            {'label': 'Accueil', 'url': 'hero'},
            {'label': 'À propos', 'url': 'about'},
            {'label': 'Compétences', 'url': 'skills'},
            {'label': 'Projets', 'url': 'projects'},
            {'label': 'Services', 'url': 'services'},
            {'label': 'Parcours', 'url': 'experience'},
            {'label': 'Contact', 'url': 'contact'},
        ],
    }