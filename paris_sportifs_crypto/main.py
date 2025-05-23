"""Point d'entree de l'application."""

from backend.api.data_integration import get_combined_data


def main() -> None:
    data = get_combined_data("football/fixtures", "https://sportsbet.io/event")
    print(data)


if __name__ == "__main__":
    main()
