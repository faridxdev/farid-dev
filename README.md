# 🐍 Portfolio Professionnel - AGBOKA FARID

Bienvenue sur le dépôt de mon portfolio personnel. Ce projet est une application web complète développée avec **Django**, conçue pour présenter mes compétences en développement backend, mes réalisations techniques et mon expertise dans l'écosystème Python.

## 🚀 Aperçu

Le portfolio adopte une esthétique "Terminal" moderne, mettant en avant une identité visuelle forte orientée "Python First". Il est entièrement dynamique et géré via une interface d'administration personnalisée.

**🌐 Démo en ligne :** [Ton lien Render ici si disponible]

## 🛠️ Stack Technique

- **Backend :** Python 3.13+, Django 6.0 (Architecture MVT)
- **API :** Django REST Framework (DRF) + Swagger/OpenAPI
- **Frontend :** Tailwind CSS, DaisyUI, HTMX (pour le dynamisme sans JS lourd)
- **Base de données :** Neon PostgreSQL (Production), SQLite (Développement)
- **Déploiement & DevOps :** Docker, Gunicorn, WhiteNoise, Render
- **IA & Vision :** OpenCV, DeepFace

## ✨ Fonctionnalités Clés

- **Gestion Dynamique :** Toutes les sections (Projets, Compétences, Formations) sont administrables via le panneau Django.
- **Formulaire de Contact AJAX :** Envoi de messages sans rechargement de page avec notifications par email (SMTP).
- **API RESTful :** Exposition des projets et articles de blog via une API documentée sous Swagger.
- **SEO & Social Sharing :** Optimisation du référencement et balises Open Graph pour un partage propre sur LinkedIn/Twitter.
- **Interface Responsive :** Design mobile-first avec sidebar interactive.

## 📂 Projets Phares

1. **PerteDocs.tg** 🇹🇬 : Plateforme de déclaration de perte de documents administratifs avec génération de PDF et upload HTMX.
2. **Système de Suivi Médical** 🏥 : Gestion interne pour clinique (Patients, Rendez-vous avec FullCalendar, Dossiers médicaux).
3. **Présence par Reconnaissance Faciale** 🤖 : Système automatisé utilisant OpenCV et DeepFace intégré à Django.
4. **KATAUPARFUM** 🛍️ : E-commerce complet avec panier session et tunnel de commande via WhatsApp.
5. **EduPlatform** 🎓 : Gestion académique sous architecture MVC.

## 💻 Installation Locale

1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/faridxdev/farid-dev.git
   cd farid-dev
   ```

2. **Créer l'environnement virtuel :**
   ```bash
   python -m venv env
   source env/Scripts/activate  # Sur Windows: env\Scripts\activate
   ```

3. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer les variables d'environnement :**
   Créez un fichier `.env` à la racine et inspirez-vous du fichier `settings.py` pour les clés secrètes et les configurations email.

5. **Migrations et lancement :**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

## 🚢 Déploiement

Le projet est optimisé pour un déploiement sur **Render** avec une base de données **Neon PostgreSQL**.
- Un script `build.sh` est inclus pour automatiser l'installation, la collecte des statiques et les migrations.
- La création du superutilisateur est automatisée via des variables d'environnement.
- Configuration prête pour **WhiteNoise** (service de fichiers statiques).
- Docker-ready pour la conteneurisation.

### Variables d'environnement requises sur Render :

| Clé | Description |
|---|---|
| `DATABASE_URL` | URL de connexion Neon PostgreSQL (ex: `postgres://user:pass@ep-...)` |
| `SECRET_KEY` | Clé secrète Django pour la production |
| `DEBUG` | Mettre à `False` |
| `DJANGO_SUPERUSER_USERNAME` | Nom d'utilisateur admin souhaité |
| `DJANGO_SUPERUSER_EMAIL` | Email de l'administrateur |
| `DJANGO_SUPERUSER_PASSWORD` | Mot de passe de l'administrateur |
| `ALLOWED_HOSTS` | Votre domaine (ex: `votre-portfolio.onrender.com`) |

## 👨‍💻 À propos de moi

Je suis **AGBOKA FARID**, développeur Backend passionné par l'architecture logicielle et la résolution de problèmes complexes. Basé à Lomé, Togo 🇹🇬.

- **GitHub :** @faridxdev
- **LinkedIn :** Agboka Farid
- **Email :** agbokafarid@gmail.com

---
*Projet développé avec passion et 🐍 Python.*