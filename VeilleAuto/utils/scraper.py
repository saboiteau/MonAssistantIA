import requests
from bs4 import BeautifulSoup
from datetime import datetime
import re

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
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        raise Exception(f"Erreur lors du téléchargement de l'URL : {e}")

    soup = BeautifulSoup(response.content, 'html.parser')

    # 1. Extraction du Titre
    title = soup.title.string.strip() if soup.title else "Titre Inconnu"
    # Nettoyage fréquent (ex: "Titre Article | Nom Site" -> "Titre Article")
    if "|" in title:
        title = title.split("|")[0].strip()
    elif " - " in title:
        title = title.split(" - ")[0].strip()

    # 2. Extraction de l'Auteur
    author = "Inconnu"
    meta_author = soup.find('meta', attrs={'name': 'author'}) or soup.find('meta', property='article:author')
    if meta_author:
        content = meta_author.get('content')
        if content:
            author = content

    # 3. Extraction de la Date
    date_str = datetime.now().strftime("%Y-%m-%d") # Par défaut : aujourd'hui
    meta_date = soup.find('meta', property='article:published_time') or \
                soup.find('meta', attrs={'name': 'date'}) or \
                soup.find('time')
    
    if meta_date:
        content = meta_date.get('content') or meta_date.get('datetime')
        if content:
            # Tentative de parsing simple (YYYY-MM-DD)
            match = re.search(r'(\d{4}-\d{2}-\d{2})', content)
            if match:
                date_str = match.group(1)

    # 4. Extraction du Texte
    # On cherche d'abord une balise <article>, sinon <main>, sinon on prend tous les <p>
    article_body = soup.find('article')
    if not article_body:
        article_body = soup.find('main')
    
    if article_body:
        paragraphs = article_body.find_all('p')
    else:
        paragraphs = soup.find_all('p')

    # Nettoyage et assemblage
    text_content = []
    for p in paragraphs:
        text = p.get_text().strip()
        if len(text) > 20: # Filtrer les paragraphes trop courts (menus, pubs...)
            text_content.append(text)
    
    raw_text = "\n\n".join(text_content)

    if not raw_text:
        raw_text = "Contenu non extrait automatiquement. Veuillez vérifier l'URL."

    return title, author, date_str, raw_text
