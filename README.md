

---

## ✅ Contenu du `README.md`

```markdown
# 🎓 Gestion des Étudiants – Projet Django

Ce projet est une application web développée avec Django permettant de **gérer une liste d’étudiants** : ajout, modification, suppression et affichage.

---

## 🚀 Fonctionnalités

- ✅ Ajouter un étudiant via un formulaire
- ✏️ Modifier les informations d’un étudiant
- 🗑️ Supprimer un étudiant
- 📋 Afficher tous les étudiants dans un tableau responsive
- 💅 Interface stylisée avec **Bootstrap 5**
- 🔒 Sécurité CSRF activée sur les formulaires

---

## 📦 Prérequis

- Python 3.10 ou +
- PostgreSQL
- Git

---

## ⚙️ Installation

1. **Cloner le projet**

```bash
git clone https://github.com/ousmane262/gestion-etudiants-django.git
cd gestion-etudiants-django
```

2. **Créer un environnement virtuel**

```bash
python -m venv env
env\Scripts\activate  # Windows
```

3. **Installer les dépendances**

```bash
pip install -r requirements.txt
```

4. **Configurer la base de données PostgreSQL**

Dans `settings.py`, adapte la section `DATABASES` :

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'etudiantsdb',
        'USER': 'postgres',
        'PASSWORD': 'votre_mot_de_passe',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

5. **Appliquer les migrations**

```bash
python manage.py migrate
```

6. **Démarrer le serveur**

```bash
python manage.py runserver
```

---

## ✨ Aperçu

<img src="https://via.placeholder.com/700x300?text=Capture+de+la+liste+des+étudiants" alt="Liste des étudiants">

---

## 🙌 Contributeur

> Développé avec ❤️ Usman**  
> [GitHub – @ousmane262](https://github.com/ousmane262)

---

## 📄 Licence

Ce projet est open source et disponible sous la licence MIT.
```

---

### ✅ Prochaine étape

1. Crée un fichier nommé `README.md` dans le dossier racine
2. Colle ce contenu
3. Fais :

```bash
git add README.md
git commit -m "📝 Ajout du README"
git push
```

