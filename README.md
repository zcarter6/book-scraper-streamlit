# Book Scraper

A Streamlit web app that scrapes books.toscrape.com by genre and keyword, then sorts the results by rating.

## Features
- Pick a genre from the site's categories
- Search book titles by keyword
- Follows pagination to collect results across multiple pages
- Sorts results by rating (highest first)
- Saves results to a text file

## Tech Used
Python, Streamlit, BeautifulSoup, Requests

## How to Run
1. Install Python from python.org
2. Download `book_scraper_zc.py` from this repo
3. Open a terminal in the folder where you saved it
4. Install the requirements:
```
python -m pip install streamlit requests beautifulsoup4
```
5. Run the app:
```
python -m streamlit run book_scraper_zc.py
```
The app opens in your browser at http://localhost:8501.

## Usage
1. Type a genre exactly as it appears on the site (e.g., Travel)
2. Enter a keyword
3. Click Search

