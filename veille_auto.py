# veille_auto.py
"""Automated Veille Script – Spec‑Driven Development

Usage:
    python veille_auto.py <URL>

Le script récupère le contenu d'un article, le résume via le LLM (Gemini 3 ou autre), crée la fiche Markdown
et met à jour le fichier d'index.
"""

import argparse
import sys
from pathlib import Path

# Import des modules utils (ils seront créés dans le même projet)
from utils.scraper import fetch
from utils.summarizer import summarize
from utils.index_updater import insert_entry
from utils.fiche_writer import write_fiche


def main():
    parser = argparse.ArgumentParser(description="Automatiser la création d'une fiche de veille à partir d'une URL.")
    parser.add_argument("url", help="URL de l'article à analyser")
    args = parser.parse_args()

    try:
        # 1️⃣ Récupérer le contenu de la page
        title, author, date, raw_text = fetch(args.url)
        metadata = {"title": title, "author": author, "date": date, "source": args.url}

        # 2️⃣ Générer la fiche via le LLM
        markdown_fiche = summarize(raw_text, metadata)

        # 3️⃣ Écrire la fiche dans le bon répertoire
        fiche_path = write_fiche(markdown_fiche, date)

        # 4️⃣ Mettre à jour l'index
        insert_entry(fiche_path, metadata)

        print(f"✅ Fiche créée : {fiche_path}")
    except Exception as e:
        print(f"❌ Erreur : {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
