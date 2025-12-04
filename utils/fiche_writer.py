from pathlib import Path
import re
import unicodedata

def slugify(value):
    """
    Normalise une chaîne pour en faire un nom de fichier sûr.
    """
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    return re.sub(r'[-\s]+', '-', value)

def write_fiche(md_content: str, date: str) -> Path:
    """
    Écrit le contenu Markdown dans un fichier structuré par date.
    """
    # 1. Extraire l'année et le mois
    try:
        year, month, _ = date.split("-")
    except ValueError:
        # Fallback date du jour
        from datetime import datetime
        now = datetime.now()
        year, month = str(now.year), f"{now.month:02d}"

    # 2. Créer le dossier cible
    target_dir = Path(f"Veille/fiches/{year}-{month}")
    target_dir.mkdir(parents=True, exist_ok=True)

    # 3. Extraire le titre pour le slug
    # On cherche la ligne "# Veille : Titre"
    match = re.search(r'^# Veille\s*:\s*(.+)$', md_content, re.MULTILINE)
    if match:
        title = match.group(1)
    else:
        title = "nouvelle-fiche"

    slug = slugify(title)
    filename = f"{slug}-{year}-{month}.md"
    file_path = target_dir / filename

    # 4. Écrire le fichier
    # Si le fichier existe déjà, on ajoute un suffixe pour ne pas écraser
    if file_path.exists():
        counter = 2
        while file_path.exists():
            filename = f"{slug}-{year}-{month}-v{counter}.md"
            file_path = target_dir / filename
            counter += 1

    file_path.write_text(md_content, encoding="utf-8")
    
    return file_path.absolute()
