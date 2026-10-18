# Web Scraper — Job Listings

Scrapes a public job listings site, extracts structured data, and saves results to CSV/JSON.

## Portfolio Description

A web scraper that collects job listings from a public site, extracts structured data (title, company, location, date), and exports results to CSV. Built with BeautifulSoup and Requests, it includes keyword filtering, deduplication across runs, and polite rate limiting. A practical demonstration of data extraction, parsing, and automation.

## Features

- Scrape job title, company, location, date posted, and URL
- Filter results by keyword or location
- Export to CSV and JSON
- Deduplication across multiple runs
- Rate limiting and request error handling

## Tech Stack

- Python 3
- `requests`, `beautifulsoup4`, `csv`, `json`, `time`

## Project Structure

```
04-web-scraper-jobs/
├── README.md
├── requirements.txt
├── output/                 # scraped data saved here
├── src/
│   ├── __init__.py
│   ├── main.py             # entry point and CLI args
│   ├── scraper.py          # HTTP requests and HTML parsing
│   ├── parser.py           # data extraction from parsed HTML
│   └── storage.py          # CSV/JSON export and deduplication
└── tests/
    └── test_parser.py
```

## Getting Started

```bash
pip install -r requirements.txt
python src/main.py
```

## Usage

```bash
# Scrape with keyword filter
python src/main.py --keyword "python developer" --location "remote"

# Save output
python src/main.py --output csv
```

## Status

🚧 In progress
