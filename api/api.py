# api/api.py
import requests
import logging
from assets.config import setup_logging
from api.auth import get_strava_tokens

# Setup logging for this module
setup_logging()
logger = logging.getLogger(__name__)


def get_strava_activities() -> None:
    """
    Fetches all Strava activities for the authenticated user.

    :return: JSON response containing Strava activities, or None if the request fails.
    """
    access_token = get_strava_tokens()
    if access_token is None:
        raise Exception("Failed to retrieve access token.")

    activities_url = "https://www.strava.com/api/v3/athlete/activities"
    headers = {"Authorization": "Bearer " + access_token}
    params = {"per_page": 200, "page": 1}

    try:
        response = requests.get(activities_url, headers=headers, params=params)
        response.raise_for_status()  # Raise exception for non-200 status codes

        return response.json()  # Return the list of activities as JSON
    except requests.exceptions.RequestException as e:
        logger.error(f"Error occurred while fetching activities: {e}")
        return None  # Return None if the request fails
