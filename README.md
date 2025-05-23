# Paris Sportifs Crypto

Ce dépôt contient les documents et le squelette de code pour un programme d'automatisation des paris sportifs utilisant les cryptomonnaies.

## Structure du code

Le dossier `paris_sportifs_crypto` présente la structure initiale décrite dans la documentation.
Vous y trouverez un backend (API, analyse, base de données, utilitaires) et un frontend minimal.

## Mise en place de l'environnement

Avant de lancer le programme, exécutez le script `setup.sh` pour installer les dépendances nécessaires et vérifier l'accès réseau :

```bash
./setup.sh
```

## Lancer un test rapide

Après la mise en place, vous pouvez lancer un test rapide :

```bash
python paris_sportifs_crypto/main.py
```

Ce script affiche des données fictives provenant des modules d'intégration.

## Configuration de l'API DeepSeek

Copiez le fichier `.env.example` vers `.env` et renseignez votre clé API :

```bash
cp .env.example .env
echo "DEEPSEEK_API_KEY=YOUR_KEY" >> .env  # remplacez YOUR_KEY par votre clé
```

Le programme chargera automatiquement cette clé pour interroger l'API DeepSeek.
