"""Intégration avec l'API DeepSeek."""

from typing import Any
from urllib import request, error
import json

from ..utils.config import API_KEY


BASE_URL = "https://api.deepseek.com/v1"


def fetch_data(endpoint: str) -> dict:
    """Recupere les données depuis l'API DeepSeek."""
    if not API_KEY:
        return {"endpoint": endpoint, "data": {"error": "cle API manquante"}}
    url = f"{BASE_URL}/{endpoint}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    req = request.Request(url, headers=headers)
    try:
        with request.urlopen(req, timeout=10) as resp:
            data: Any = json.load(resp)
    except error.URLError:
        data = {"error": "reseau indisponible"}
    return {"endpoint": endpoint, "data": data}
