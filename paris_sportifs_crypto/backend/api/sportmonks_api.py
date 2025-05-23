"""Intégration avec l'API DeepSeek."""

from typing import Any
import requests

from ..utils.config import API_KEY


BASE_URL = "https://api.deepseek.com/v1"


def fetch_data(endpoint: str) -> dict:
    """Recupere les données depuis l'API DeepSeek."""
    if not API_KEY:
        raise ValueError("DEEPSEEK_API_KEY non configuree")
    url = f"{BASE_URL}/{endpoint}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    data: Any = response.json()
    return {"endpoint": endpoint, "data": data}
