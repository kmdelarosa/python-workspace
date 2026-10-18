"""HTTP requests and HTML parsing for job listings."""
import time
import requests
from bs4 import BeautifulSoup

# Practice target — replace with actual job board URL
BASE_URL = "https://quotes.toscrape.com"


def fetch_listings(keyword: str = "", location: str = "") -> list[dict]:
    """Fetch and parse job listings. Returns a list of listing dicts."""
    listings = []
    try:
        response = requests.get(BASE_URL, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        listings = _parse_listings(soup, keyword, location)
    except requests.RequestException as e:
        print(f"Request failed: {e}")

    time.sleep(1)  # polite rate limiting
    return listings


def _parse_listings(soup: BeautifulSoup, keyword: str, location: str) -> list[dict]:
    """Extract listing data from parsed HTML. Update selectors for your target site."""
    listings = []
    # TODO: update selectors to match target job board HTML structure
    items = soup.select(".job-listing")
    for item in items:
        title = item.select_one(".job-title")
        company = item.select_one(".company")
        loc = item.select_one(".location")
        date = item.select_one(".date-posted")
        link = item.select_one("a")

        listing = {
            "title": title.text.strip() if title else "",
            "company": company.text.strip() if company else "",
            "location": loc.text.strip() if loc else "",
            "date_posted": date.text.strip() if date else "",
            "url": link["href"] if link else "",
        }

        if _matches_filter(listing, keyword, location):
            listings.append(listing)

    return listings


def _matches_filter(listing: dict, keyword: str, location: str) -> bool:
    keyword_match = not keyword or keyword.lower() in listing["title"].lower()
    location_match = not location or location.lower() in listing["location"].lower()
    return keyword_match and location_match
