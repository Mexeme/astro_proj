
# astro_proj

**astro_proj** est un projet Python qui permet de réaliser divers calculs astronomiques, y compris la conversion d'unités et le calcul de la luminosité d'étoiles. Le projet fournit une interface utilisateur permettant de choisir différentes options via un menu interactif dans le terminal.

## Fonctionnalités

- **Calcul de la luminosité d'une étoile** : Le projet permet de calculer la luminosité d'une étoile en fonction de sa température et de son rayon, en utilisant des formules astronomiques standards.
- **Conversion d'unités** : Conversion entre différentes unités de mesure, telles que les unités astronomiques (UA), les kilomètres, etc.
- **Gestion des erreurs** : Le programme gère les entrées invalides pour assurer une utilisation robuste et fournit des messages d'erreur appropriés.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé Python 3.6 ou une version ultérieure. Vous aurez également besoin de `unittest` pour les tests.

## Installation

1. Clonez le dépôt sur votre machine locale :
   ```bash
   git clone https://github.com/Mexeme/astro_proj.git
   ```

2. Naviguez dans le répertoire du projet :
   ```bash
   cd astro_proj
   ```

3. Créez un environnement virtuel (recommandé) et activez-le :
   - Sous Windows :
     ```bash
     python -m venv env
     .\env\Scripts\activate
     ```
   - Sous macOS/Linux :
     ```bash
     python3 -m venv env
     source env/bin/activate
     ```

4. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. Lancez le programme avec la commande suivante :
   ```bash
   python main.py
   ```

2. Vous serez invité à choisir une option dans un menu interactif :
   - **1** : Calculer la luminosité d'une étoile.
   - **2** : Effectuer une conversion d'unités.
   - **3** : Quitter le programme.

3. Pour chaque option, vous serez guidé pour entrer les données nécessaires. Le programme affichera les résultats correspondants ou des messages d'erreur en cas d'entrée invalide.

## Tests

Le projet comprend des tests unitaires pour valider le bon fonctionnement des fonctionnalités principales. Les tests sont organisés dans le répertoire `tests`.

### Lancer les tests

Pour exécuter les tests avec `unittest`, utilisez la commande suivante :
```bash
python -m unittest discover tests
```

Cela exécutera tous les tests dans le répertoire `tests`. Si vous utilisez `coverage` pour mesurer la couverture des tests, vous pouvez également exécuter les tests avec :
```bash
coverage run -m unittest discover tests
coverage report
```

## Contribuer

Si vous souhaitez contribuer à ce projet, n'hésitez pas à soumettre une **pull request**. Voici comment vous pouvez contribuer :

1. Fork le dépôt.
2. Créez une branche pour votre fonctionnalité ou correction de bug.
3. Faites vos modifications.
4. Assurez-vous que les tests passent en exécutant `python -m unittest discover tests`.
5. Soumettez une pull request.

## Licence

Ce projet est sous la licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus d'informations.

---

Merci d'utiliser **astro_proj** !
