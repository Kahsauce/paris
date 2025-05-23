"""Scraper ethique pour Sportsbet.io."""

from urllib import request, error
import time


def scrape_odds(event_url: str, retries: int = 3, delay: float = 2.0) -> dict:
    """Recupere les cotes en tentant plusieurs fois en cas d'echec reseau."""
    for attempt in range(retries):
        try:
            with request.urlopen(event_url, timeout=10) as resp:
                # Le parsing HTML n'est pas encore implémenté
                html = resp.read().decode("utf-8", "ignore")
            return {"url": event_url, "html": html}
        except error.URLError as exc:
            last_error = str(exc.reason)
            if attempt < retries - 1:
                time.sleep(delay)

    return {"url": event_url, "error": last_error or "reseau indisponible"}
