import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch(url: str):
    """
    Récupère le contenu d'une page web et extrait les métadonnées.

    Args:
        url (str): L'URL de l'article à scraper.

    Returns:
        tuple: (title, author, date, raw_text)
            - title (str): Titre de l'article.
            - author (str): Auteur de l'article (ou "Inconnu").
            - date (str): Date de publication (YYYY-MM-DD) ou date du jour.
            - raw_text (str): Texte brut de l'article.
    
    Raises:
        Exception: Si le téléchargement ou le parsing échoue.
    """
    # TODO: Implémenter la logique de scraping avec requests et BeautifulSoup
    # 1. Télécharger la page
    # 2. Parser le HTML
    # 3. Extraire les infos
    pass
