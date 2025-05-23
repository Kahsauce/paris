"""Intégration avec l'API DeepSeek."""

from typing import Any
from urllib import request, error
import json
import time

from ..utils.config import API_KEY


BASE_URL = "https://api.deepseek.com/v1"


def fetch_data(endpoint: str, retries: int = 3, delay: float = 2.0) -> dict:
    """Recupere les données depuis l'API DeepSeek en reessayant en cas d'echec."""
    if not API_KEY:
        return {"endpoint": endpoint, "data": {"error": "cle API manquante"}}

    url = f"{BASE_URL}/{endpoint}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    req = request.Request(url, headers=headers)

    last_error: str | None = None
    for attempt in range(retries):
        try:
            with request.urlopen(req, timeout=10) as resp:
                data: Any = json.load(resp)
            return {"endpoint": endpoint, "data": data}
        except error.URLError as exc:
            last_error = str(exc.reason)
            if attempt < retries - 1:
                time.sleep(delay)

    return {"endpoint": endpoint, "data": {"error": last_error or "reseau indisponible"}}
