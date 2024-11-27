# Pierre-Feuille-Ciseaux Simulation Game

Ce projet implémente une simulation du jeu **Pierre-Feuille-Ciseaux** dans un environnement graphique à l'aide de la bibliothèque `pygame`. Les objets "Pierre", "Feuille", et "Ciseaux" se déplacent aléatoirement sur une carte, interagissent selon les règles du jeu, et jouent des sons spécifiques lorsqu'ils entrent en collision.

## Fonctionnalités
- Simulation dynamique avec des objets interactifs.
- Graphismes personnalisés pour chaque type d'objet.
- Sons spécifiques joués lors des interactions entre objets.
- Paramètres configurables pour la taille de la carte, le nombre d'objets, et les FPS.

---

## Structure du projet

### 1. **Fichiers principaux**
- **`main.py`** : Point d'entrée du jeu, initialise l'environnement, gère la boucle principale, et affiche les objets.
- **`game.py`** : Contient la logique principale du jeu, comme la création d'objets, la détection des collisions, et leur comportement.
- **`objet.py`** : Définit la classe `Objet` pour gérer les entités graphiques (pierre, feuille, ciseaux).
- **`sounds.py`** : Gère les sons joués pendant le jeu.

### 2. **Dossier assets**
Ce répertoire contient :
- Les images utilisées pour représenter les objets.
- Les fichiers audio associés aux interactions.

---

## Installation

### 1. Prérequis
- Python 3.10 ou supérieur.
- Bibliothèques Python :
  - `pygame`
  - `Pillow` pour le redimensionnement des images.

Installez les dépendances avec la commande :
```bash
pip install pygame pillow
