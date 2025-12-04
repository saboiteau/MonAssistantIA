from pathlib import Path

def insert_entry(fiche_path: Path, metadata: dict):
    """
    Met à jour le fichier Veille/index.md avec la nouvelle fiche.

    Args:
        fiche_path (Path): Chemin absolu vers le fichier fiche créé.
        metadata (dict): Métadonnées de l'article.
    """
    # TODO:
    # 1. Lire le fichier index.md
    # 2. Trouver la section du mois correspondant (ex: "### Décembre 2025")
    # 3. Insérer la ligne "- **[YYYY-MM-DD]** [Titre](chemin_relatif) - Résumé court"
    # 4. Mettre à jour le compteur de stats
    # 5. Sauvegarder
    pass
