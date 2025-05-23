"""Scraper ethique pour Sportsbet.io avec respect du ``robots.txt``."""

from __future__ import annotations

from pathlib import Path
from urllib import request, error, parse, robotparser
import hashlib
import time


USER_AGENT = "ParisCryptoBot/1.0"
CACHE_DIR = Path(__file__).resolve().parents[2] / "cache"


def _is_allowed(url: str, user_agent: str = USER_AGENT) -> bool:
    """Verifie si ``url`` est autorise par ``robots.txt``."""
    parsed = parse.urlparse(url)
    robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"
    rp = robotparser.RobotFileParser()
    rp.set_url(robots_url)
    try:
        rp.read()
    except Exception:
        return False
    return rp.can_fetch(user_agent, url)


def _cache_path(url: str) -> Path:
    digest = hashlib.md5(url.encode()).hexdigest()
    CACHE_DIR.mkdir(exist_ok=True)
    return CACHE_DIR / f"{digest}.html"


def scrape_odds(event_url: str, retries: int = 3, delay: float = 2.0) -> dict:
    """Recupere les cotes en respectant les regles d'acces du site."""
    if not _is_allowed(event_url):
        return {"url": event_url, "error": "interdit par robots.txt"}

    cache_file = _cache_path(event_url)
    if cache_file.is_file():
        html = cache_file.read_text(encoding="utf-8")
        return {"url": event_url, "html": html, "cached": True}

    last_error: str | None = None
    for attempt in range(retries):
        try:
            req = request.Request(event_url, headers={"User-Agent": USER_AGENT})
            with request.urlopen(req, timeout=10) as resp:
                html = resp.read().decode("utf-8", "ignore")
            cache_file.write_text(html, encoding="utf-8")
            return {"url": event_url, "html": html}
        except error.URLError as exc:
            last_error = str(exc.reason)
            if attempt < retries - 1:
                time.sleep(delay)

    return {"url": event_url, "error": last_error or "reseau indisponible"}
