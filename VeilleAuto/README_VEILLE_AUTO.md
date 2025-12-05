# 🤖 Automatisateur de Veille (Spec-DD)

Ce script permet de générer automatiquement une fiche de veille à partir d'une URL, en utilisant l'IA (Gemini, OpenAI ou Anthropic) pour le résumé, et met à jour l'index automatiquement.

## 🚀 Installation

1.  **Prérequis** : Avoir Python installé.
2.  **Installer les dépendances** :
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configurer les clés API** :
    *   Copiez le fichier `.env.example` en `.env` :
        ```bash
        copy .env.example .env
        ```
    *   Ouvrez `.env` et ajoutez votre clé API Gemini :
        ```
        GEMINI_API_KEY=votre_clé_ici
        LLM_PROVIDER=gemini
        ```

## 🎮 Utilisation

### Mode 1 : Traitement d'une URL unique (Ligne de commande)

```bash
python veille_auto.py "https://lien-de-votre-article.com"
```

### Mode 2 : Watchdog (Recommandé pour iPhone/Mobile) 🌟

**C'est le mode "Fire and Forget" parfait pour vous !**

1.  **Lancez le Watchdog** (une seule fois au démarrage de votre PC) :
    ```bash
    python veille_auto.py --watch
    ```
    Le script tourne en arrière-plan et surveille le fichier `INPUT_URLS.txt`.

2.  **Depuis n'importe où (iPhone, Chrome, Mail)** :
    *   Ouvrez le fichier `INPUT_URLS.txt` (synchronisé via OneDrive/Dropbox).
    *   Collez une URL (une par ligne).
    *   Sauvegardez.

3.  **Magie** ✨ :
    *   Le Watchdog détecte la nouvelle URL (toutes les 5 secondes).
    *   Il crée la fiche automatiquement.
    *   Il met à jour l'index.
    *   Il déplace l'URL dans `PROCESSED_URLS.txt` (historique).

### 📱 Configuration iPhone (Raccourci Siri)

Pour ajouter une URL depuis Safari/Mail en 1 clic :

1.  Ouvrez l'app **Raccourcis** sur iPhone.
2.  Créez un nouveau raccourci :
    *   **Action 1** : "Obtenir l'URL de l'entrée"
    *   **Action 2** : "Ajouter à la fin du fichier" → Sélectionnez `INPUT_URLS.txt` (dans OneDrive/iCloud)
3.  Nommez-le "Ajouter à ma Veille".
4.  Activez "Afficher dans le menu Partager".

**Résultat** : Depuis n'importe quelle app, "Partager" → "Ajouter à ma Veille" → L'URL est ajoutée au fichier → Le Watchdog la traite automatiquement.

## 🔧 Dépannage

*   **Erreur `ModuleNotFoundError`** : Vérifiez que vous avez bien lancé `pip install -r requirements.txt`.
*   **Erreur API** : Vérifiez votre clé dans `.env`.
*   **Contenu vide** : Certains sites bloquent les scrapers. Le script créera quand même une fiche, mais avec un texte par défaut.
*   **Le Watchdog ne détecte pas les URLs** : Vérifiez que le fichier `INPUT_URLS.txt` est bien dans le même dossier que `veille_auto.py`.

## 🏗️ Architecture (Spec-DD)

Ce projet a été généré en suivant la méthodologie **Spec-Driven Development**.
*   `veille_auto.py` : Chef d'orchestre + Mode Watchdog.
*   `utils/scraper.py` : Extraction web.
*   `utils/summarizer.py` : Intelligence (LLM).
*   `utils/fiche_writer.py` : Gestion fichiers.
*   `utils/index_updater.py` : Gestion index.
*   `INPUT_URLS.txt` : File d'attente des URLs à traiter.
*   `PROCESSED_URLS.txt` : Historique des URLs traitées.
