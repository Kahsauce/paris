"""Configuration du programme."""

from pathlib import Path
import os


def _load_env() -> None:
    """Charge le fichier .env situe a la racine du projet si present."""
    env_path = Path(__file__).resolve().parents[3] / ".env"
    if env_path.is_file():
        with open(env_path) as env_file:
            for line in env_file:
                if "=" in line:
                    key, value = line.strip().split("=", 1)
                    os.environ.setdefault(key, value)


_load_env()

API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
