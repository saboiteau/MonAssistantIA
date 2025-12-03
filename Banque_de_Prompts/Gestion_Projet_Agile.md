# ⚡ Gestion de Projet & Agile

## Transformation Réunion en User Stories
**Tag :** #Productivity #Agile #Meeting #Jira

### 📄 Le Problème
Après un brainstorming, la double peine : rédiger le CR + créer les tickets Jira manuellement.

### 🤖 Le Prompt
> "À partir de la transcription de réunion suivante, génère deux livrables distincts :
> 
> 1. **Un compte rendu synthétique** des décisions, à partager aux participants.
> 2. **Une liste d'actions converties en User Stories**. Pour chaque action identifiée, utilise le modèle suivant pour la rédiger :
> 
> **Titre :** [Titre clair de l'action]
> **User Story :** 'En tant que [Persona pertinent], je veux [Objectif de l'action] afin de [Bénéfice attendu].'
> **Critères d'Acceptation :**
> *   [Critère 1]
> *   [Critère 2]
> *   [Critère 3]
> **Suggestion :** Suggérer le rôle ou la personne la plus pertinente pour cette tâche."

### 💡 Astuce
Donnez la transcription brute (Teams/Meet) à l'IA. Elle fera le tri entre le bruit et les actions.

---

## Agent "Coach Rétro" pour Rétrospectives Approfondies
**Tag :** #Agile #Retrospective #TeamDynamics #ContinuousImprovement

### 📄 Le Problème
Vos rétrospectives tournent en rond. L'équipe évoque toujours les mêmes problèmes de surface ("pas assez de communication", "réunions trop longues") sans jamais creuser. Le format est répétitif et l'énergie de l'équipe diminue 📉.

### 🤖 Le Prompt - Configuration de l'Agent

> "Tu es 'Le Coach Rétro', un expert en dynamique d'équipe et en amélioration continue. Tu as deux modes :
> 
> **Mode 'Game Master' 🎲** : Quand je te le demande, propose-moi 3 formats de rétrospective créatifs (ex: 'Le Bateau de Vitesse', 'Les 4L', 'L'Étoile de Mer') et explique brièvement l'objectif et les règles de chacun.
> 
> **Mode 'Analyste de Systèmes' 📈** : Quand je te fournis le contenu anonymisé de plusieurs rétrospectives, analyse l'ensemble pour identifier les thèmes récurrents, les contradictions et suggère 2-3 hypothèses sur les causes profondes des problèmes."

### 💡 Astuce - Utilisation Bi-Modale

**Avant la réunion :** Demandez-lui de vous suggérer des formats de rétrospective originaux pour briser la routine.

**Après la réunion :** Donnez-lui les post-it anonymisés de plusieurs rétrospectives passées pour qu'il identifie les schémas récurrents et les problèmes systémiques que l'équipe ne voit plus.

### 🎯 Formats Créatifs Suggérés
- **Le Bateau de Vitesse** : Métaphore navigation (vent favorable, ancres, récifs à éviter)
- **Les 4L** : Liked, Learned, Lacked, Longed for
- **L'Étoile de Mer** : Start, Stop, Continue, More of, Less of

### 📊 Analyse Systémique
L'agent révèle les **angles morts cognitifs** de l'équipe en analysant l'historique des rétrospectives pour passer des symptômes (surface) aux causes profondes (structure).

