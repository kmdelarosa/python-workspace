"""Entry point for the Job Listings Scraper."""
import argparse
from scraper import fetch_listings
from storage import save_results


def main():
    parser = argparse.ArgumentParser(description="Job Listings Web Scraper")
    parser.add_argument("--keyword", default="", help="Filter by keyword")
    parser.add_argument("--location", default="", help="Filter by location")
    parser.add_argument("--output", choices=["csv", "json", "both"], default="csv")
    args = parser.parse_args()

    print(f"Scraping listings... keyword='{args.keyword}' location='{args.location}'")
    listings = fetch_listings(keyword=args.keyword, location=args.location)
    save_results(listings, format=args.output)
    print(f"Done. {len(listings)} listings saved.")


if __name__ == "__main__":
    main()
