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
    
    # Veille : {metadata.get('title')}

    - **Source** : [{metadata.get('source')}]({metadata.get('source')})
    - **Date** : {metadata.get('date')}
    - **Auteur** : {metadata.get('author')}
    - **Tags** : #Tag1 #Tag2 #Tag3 (à déduire du contenu, max 5 tags pertinents)

    ## 📝 Résumé
    [Rédige un résumé structuré de l'article en français. Utilise des listes à puces si nécessaire. Met en avant les points clés.]

    ## 🧠 Analyse & Pense-bête
    [Ton analyse critique : pourquoi c'est important ? Quel impact pour moi (développeur/manager IA) ? Idées d'application concrète.]
    
    ---
    
    Texte à analyser :
    {text[:15000]} 
    """
    # Note: on tronque à 15000 caractères pour rester dans les limites raisonnables des context windows standards, 
    # bien que Gemini puisse en prendre beaucoup plus.

    try:
        if PROVIDER == "openai":
            response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2,
            )
            return response.choices[0].message.content

        elif PROVIDER == "anthropic":
            response = client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=2000,
                temperature=0.2,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.content[0].text

        elif PROVIDER == "gemini":
            # Utilisation de Gemini 1.5 Flash (rapide et efficace pour du résumé)
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(prompt)
            return response.text

        else:
            return "Erreur : Provider LLM non supporté ou mal configuré. Vérifiez votre fichier .env"

    except Exception as e:
        return f"Erreur lors de la génération du résumé avec {PROVIDER} : {str(e)}"
