import requests
from django.conf import settings


def fetch_movies_from_api(page):
    url = f"https://demo.credy.in/api/v1/maya/movies/?page={page}"

    try:
        response = requests.get(url, auth=(settings.API_USERNAME, settings.API_PASSWORD))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.SSLError:
        return {"error": "SSL verification failed"}
    except requests.exceptions.RequestException:
        return {"error": "Failed to fetch movies"}
