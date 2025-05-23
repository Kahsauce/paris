#!/usr/bin/env bash
# Script d'installation des dependances pour l'environnement Codex
set -e

if [ "$EUID" -ne 0 ]; then
  echo "Ce script doit etre execute en tant que root" >&2
  exit 1
fi

# Mise a jour et installation de pip si necessaire
echo "[Setup] Installation de python3-pip"
apt-get update && apt-get install -y python3-pip curl

# Mise a niveau de pip et installation des dependances Python
echo "[Setup] Installation des dependances Python"
pip3 install --upgrade pip
if [ -f requirements.txt ]; then
  pip3 install -r requirements.txt
fi

# Test rapide de la connectivite reseau
if curl -I https://example.com > /dev/null 2>&1; then
  echo "[Setup] Acces reseau verifie avec succes"
else
  echo "[Setup] Impossible de joindre Internet" >&2
fi

echo "[Setup] Terminé"
