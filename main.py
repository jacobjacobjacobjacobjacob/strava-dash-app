# main.py
import pandas as pd
import logging

from api.update_data import fetch_strava_data
from assets.utils import create_dataframe, save_to_csv
from modules.processing import clean_data

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main(csv_file: str = "data/raw_data.csv") -> pd.DataFrame:
    """
    Main function to process Strava data from a CSV file.

    This function performs the following steps:
    1. Reads raw data from the specified CSV file.
    2. Checks if the raw data is empty and logs a warning if it is.
    3. Cleans and processes the data.
    4. Saves the cleaned data to a new CSV file.
    5. Returns the cleaned DataFrame.

    :param csv_file: Path to the CSV file containing raw data. Defaults to "data/raw_data.csv".
    :type csv_file: str

    :return: A DataFrame containing the cleaned and processed data, or None if an error occurs.
    :rtype: pd.DataFrame or None
    """
    try:
        # Load raw data
        raw_data = create_dataframe(csv_file)

        if raw_data.empty:
            logger.warning("The raw data is empty. No processing will be done.")
            return None

        # Clean and process data
        clean_df = clean_data(raw_data)

        # Save the cleaned data to a CSV file
        save_to_csv(clean_df, "clean_data")
        logger.info("Cleaned data successfully saved to 'clean_data.csv'.")

        return clean_df

    except Exception as e:
        logger.error("An error occurred during processing:", exc_info=True)
        return None


if __name__ == "__main__":
    # Fetch fresh Strava data
    fetch_strava_data()

    # Process the fetched data
    df = main()
    
