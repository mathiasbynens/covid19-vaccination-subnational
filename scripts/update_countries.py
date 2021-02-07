"""Update country data."""


import os
import argparse
from covid_updater.scraping import get_country_scraper


ISO_CODES = [
    #'AR', 'AT', 'BE', 'BR', 'CA', 'CL', 'CZ', 'DK', 'FR', 'DE',
    #'IN', 'IT', 'NO', 'PL', 'SK', 'ES', 'SE', 'CH', 'US', 'GB'
    'BE'
]
OUTPUT_PATH = os.path.join("data", "countries")


def get_parser():
    parser = argparse.ArgumentParser(description="Update country data.")
    parser.add_argument(
        "output_data_folder",
        type=str,
        help="Path to folder to export country csv data."
    )
    parser.add_argument(
        "output_info_path",
        type=str,
        help="Path to file to export source info data file."
    )
    args = parser.parse_args()
    return parser

def main():
    parser = get_parser()
    args = parser.parse_args()
    for iso_code in ISO_CODES:
        scraper = get_country_scraper(iso_code=iso_code)
        print(scraper.country)
        scraper.run(
            output_file_data=os.path.join(args.output_data_folder, f"{scraper.filename}.csv"),
            output_file_info=args.output_info_path,
        )


if __name__ == "__main__":
    main()