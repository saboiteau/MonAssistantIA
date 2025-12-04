from pathlib import Path
import re
from datetime import datetime

INDEX_PATH = Path("Veille/index.md")

def insert_entry(fiche_path: Path, metadata: dict):
    """
    Met à jour le fichier Veille/index.md avec la nouvelle fiche.
    """
    if not INDEX_PATH.exists():
        print(f"⚠️ Attention : {INDEX_PATH} introuvable. Création d'un index vierge.")
        INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
        INDEX_PATH.write_text("# Veille Technologique\n\n## Chronologie\n\n## Statistiques\n- **Total d'articles** : 0\n", encoding="utf-8")

    content = INDEX_PATH.read_text(encoding="utf-8")
    
    # 1. Préparer la ligne à insérer
    # Format : - **[YYYY-MM-DD]** [Titre](chemin_relatif) - Auteur/Source
    # On calcule le chemin relatif depuis le dossier Veille/
    try:
        relative_path = fiche_path.relative_to(INDEX_PATH.parent).as_posix()
    except ValueError:
        # Fallback si les chemins ne correspondent pas (ex: test local)
        relative_path = fiche_path.name

    new_line = f"- **[{metadata['date']}]** [{metadata['title']}]({relative_path}) - {metadata['author']}"

    # 2. Trouver ou créer la section du mois
    # On parse la date pour avoir le mois en français (approximatif ou via mapping)
    try:
        date_obj = datetime.strptime(metadata['date'], "%Y-%m-%d")
    except ValueError:
        date_obj = datetime.now()

    mois_map = {
        1: "Janvier", 2: "Février", 3: "Mars", 4: "Avril", 5: "Mai", 6: "Juin",
        7: "Juillet", 8: "Août", 9: "Septembre", 10: "Octobre", 11: "Novembre", 12: "Décembre"
    }
    mois_annee = f"{mois_map[date_obj.month]} {date_obj.year}"
    section_header = f"### {mois_annee}"

    if section_header in content:
        # La section existe, on insère après le header
        # On cherche la position du header
        pattern = re.escape(section_header)
        match = re.search(pattern, content)
        if match:
            end_pos = match.end()
            # On insère une nouvelle ligne après le header
            content = content[:end_pos] + "\n\n" + new_line + content[end_pos:]
    else:
        # La section n'existe pas, on doit la créer au début de la chronologie (après le premier header ##)
        # On cherche "## Chronologie" ou le premier "### "
        chrono_header = "## Chronologie"
        if chrono_header in content:
            pattern = re.escape(chrono_header)
            match = re.search(pattern, content)
            if match:
                end_pos = match.end()
                new_section = f"\n\n{section_header}\n\n{new_line}"
                content = content[:end_pos] + new_section + content[end_pos:]
        else:
            # Fallback : on ajoute à la fin si on ne trouve pas la structure
            content += f"\n\n{section_header}\n\n{new_line}"

    # 3. Mettre à jour les statistiques
    # On cherche "- **Total d'articles** : X"
    stats_pattern = r"(- \*\*Total d'articles\*\* : )(\d+)"
    match_stats = re.search(stats_pattern, content)
    if match_stats:
        prefix = match_stats.group(1)
        current_count = int(match_stats.group(2))
        new_count = current_count + 1
        content = re.sub(stats_pattern, f"{prefix}{new_count}", content)

    # 4. Sauvegarder
    INDEX_PATH.write_text(content, encoding="utf-8")
    print(f"✅ Index mis à jour : Ajouté dans '{mois_annee}' et compteur incrémenté.")
