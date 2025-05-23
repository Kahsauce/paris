"""Fusion des donnees provenant de differentes sources."""


from .sportmonks_api import fetch_data
from .sportsbet_scraper import scrape_odds


def get_combined_data(endpoint: str, event_url: str) -> dict:
    """Combine les donnees de l'API et du scraping."""
    api_data = fetch_data(endpoint)
    odds = scrape_odds(event_url)
    return {"api": api_data, "odds": odds}
