"""Automated Veille Script – Watchdog Mode

Usage:
    python veille_auto.py [--watch]

Mode Watchdog : Surveille le fichier INPUT_URLS.txt et traite les URLs ajoutées.
Mode One-shot : python veille_auto.py <URL>
"""

import argparse
import sys
import time
import shutil
from pathlib import Path
from datetime import datetime

# Import des modules utils
from utils.scraper import fetch
from utils.summarizer import summarize
from utils.index_updater import insert_entry
from utils.fiche_writer import write_fiche

INPUT_FILE = Path("INPUT_URLS.txt")
PROCESSED_FILE = Path("PROCESSED_URLS.txt")

def process_url(url):
    """Traite une URL unique : Scrape -> Summarize -> Write -> Index"""
    print(f"🔄 Traitement de : {url}")
    try:
        title, author, date, raw_text = fetch(url)
        metadata = {"title": title, "author": author, "date": date, "source": url}
        
        markdown_fiche = summarize(raw_text, metadata)
        fiche_path = write_fiche(markdown_fiche, date)
        insert_entry(fiche_path, metadata)
        
        print(f"✅ Succès : {fiche_path.name}")
        return True
    except Exception as e:
        print(f"❌ Erreur sur {url} : {e}", file=sys.stderr)
        return False

def watchdog_mode():
    """Surveille le fichier INPUT_URLS.txt en boucle"""
    print(f"👀 Mode Watchdog activé. Surveillance de {INPUT_FILE.absolute()}...")
    print("Appuyez sur Ctrl+C pour arrêter.")
    
    while True:
        # Git pull pour récupérer les modifications depuis GitHub
        try:
            import subprocess
            result = subprocess.run(['git', 'pull'], capture_output=True, text=True, timeout=10)
            if 'Already up to date' not in result.stdout:
                print(f"🔄 Git pull : {result.stdout.strip()}")
        except Exception as e:
            print(f"⚠️ Git pull échoué (normal si pas de connexion) : {e}")
        
        if INPUT_FILE.exists():
            # Lire les URLs
            with open(INPUT_FILE, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            urls_to_process = [line.strip() for line in lines if line.strip() and not line.strip().startswith('#')]
            
            if urls_to_process:
                print(f"detecté {len(urls_to_process)} URLs à traiter.")
                
                remaining_lines = []
                
                for line in lines:
                    url = line.strip()
                    if not url or url.startswith('#'):
                        remaining_lines.append(line)
                        continue
                        
                    success = process_url(url)
                    
                    # Log dans PROCESSED_URLS
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    status = "OK" if success else "ERROR"
                    with open(PROCESSED_FILE, 'a', encoding='utf-8') as hist:
                        hist.write(f"[{timestamp}] [{status}] {url}\n")
                
                # Vider le fichier d'entrée (ou ne garder que les commentaires)
                # Ici on choisit de vider les URLs traitées pour éviter de les refaire
                with open(INPUT_FILE, 'w', encoding='utf-8') as f:
                    f.writelines(remaining_lines)
                
                # Git commit et push pour synchroniser
                try:
                    import subprocess
                    subprocess.run(['git', 'add', '.'], timeout=5)
                    subprocess.run(['git', 'commit', '-m', f'Auto: Traité {len(urls_to_process)} URLs'], timeout=5)
                    subprocess.run(['git', 'push'], timeout=10)
                    print("📤 Modifications synchronisées sur GitHub")
                except Exception as e:
                    print(f"⚠️ Git sync échoué : {e}")
                    
        time.sleep(5) # Vérifier toutes les 5 secondes

def main():
    parser = argparse.ArgumentParser(description="Automatiser la veille.")
    parser.add_argument("url", nargs="?", help="URL unique à traiter")
    parser.add_argument("--watch", action="store_true", help="Activer le mode surveillance de fichier")
    
    args = parser.parse_args()

    if args.watch:
        try:
            watchdog_mode()
        except KeyboardInterrupt:
            print("\n🛑 Arrêt du Watchdog.")
    elif args.url:
        process_url(args.url)
    else:
        print("Usage: python veille_auto.py <URL> OU python veille_auto.py --watch")

if __name__ == "__main__":
    main()
