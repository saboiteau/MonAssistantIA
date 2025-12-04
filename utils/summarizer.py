import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Configuration du provider LLM
PROVIDER = os.getenv("LLM_PROVIDER", "openai").lower()

# Initialisation des clients selon le provider
if PROVIDER == "openai":
    import openai
    openai.api_key = os.getenv("LLM_API_KEY")
elif PROVIDER == "anthropic":
    import anthropic
    client = anthropic.Anthropic(api_key=os.getenv("LLM_API_KEY"))
elif PROVIDER == "gemini":
    import google.generativeai as genai
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def summarize(text: str, metadata: dict) -> str:
    """
    Génère une fiche de veille au format Markdown via un LLM.

    Args:
        text (str): Le texte brut de l'article.
        metadata (dict): Métadonnées (titre, auteur, date, source).

    Returns:
        str: Le contenu Markdown de la fiche générée.
    """
    
    # Prompt système pour guider le LLM
    prompt = f"""
    Tu es mon assistant éditorial expert en veille technologique.
    Ta mission est de générer une fiche de veille structurée au format Markdown à partir du texte ci-dessous.
    
    Respecte scrupuleusement ce format :
    
    # Veille : [Titre de l'article]

    - **Source** : [{metadata.get('source')}]({metadata.get('source')})
    - **Date** : {metadata.get('date')}
    - **Auteur** : {metadata.get('author')}
    - **Tags** : #Tag1 #Tag2 #Tag3 (à déduire du contenu)

    ## 📝 Résumé
    [Résumé structuré de l'article en français. Met en avant les points clés.]

    ## 🧠 Analyse & Pense-bête
    [Ton analyse critique : pourquoi c'est important ? Quel impact pour moi ? Idées d'application concrète.]
    
    ---
    
    Texte à analyser :
    {text[:10000]} # On tronque pour éviter de dépasser les limites de tokens si nécessaire
    """

    try:
        if PROVIDER == "openai":
            # TODO: Appel API OpenAI
            pass
        elif PROVIDER == "anthropic":
            # TODO: Appel API Anthropic
            pass
        elif PROVIDER == "gemini":
            # TODO: Appel API Gemini
            pass
        else:
            return "Erreur : Provider LLM non supporté ou mal configuré."
            
        # Placeholder pour le moment
        return f"# Fiche générée (Simulation)\n\nContenu basé sur {metadata['title']}"

    except Exception as e:
        return f"Erreur lors de la génération du résumé : {str(e)}"
