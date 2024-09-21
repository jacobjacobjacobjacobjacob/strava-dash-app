# assets/config.py
import pytz
import logging

STRAVA_DATA_PATH = "/Users/daniel/Desktop/python/strava-dash-app/data/clean_data.csv"
DASHAPP_TITLE = "Strava Dashboard"

BIKE_DURATION_GOAL_2024 = 200
BIKE_DISTANCE_GOAL_2024 = 2000
RUN_DISTANCE_GOAL_2024 = 200
RUN_DURATION_GOAL_2024 = 20

# Set up max_hr, weight_kg and stride_lenght in assets/health_data.py

local_tz = pytz.timezone("Europe/Oslo")  # Timezone
ignored_tzs = ["(GMT-10:00) Pacific/Honolulu", "(GMT-08:00) America/Los_Angeles"]


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
