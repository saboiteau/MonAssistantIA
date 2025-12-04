from pathlib import Path
import re

def write_fiche(md_content: str, date: str) -> Path:
    """
    Écrit le contenu Markdown dans un fichier structuré par date.

    Args:
        md_content (str): Le contenu de la fiche.
        date (str): La date de publication (YYYY-MM-DD).

    Returns:
        Path: Le chemin absolu du fichier créé.
    """
    # TODO:
    # 1. Extraire l'année et le mois de la date
    # 2. Créer le dossier Veille/fiches/YYYY-MM s'il n'existe pas
    # 3. Générer un nom de fichier "slugifié" (ex: titre-article-2025-12.md)
    # 4. Écrire le fichier
    pass
