# IMDb Movie Data Scraper

Welcome to the IMDb Movie Data Scraper project! This repository contains a Python script to scrape movie data from IMDb using requests and BeautifulSoup libraries. As a machine learning developer and data scientist, you can use this script to collect movie data for various data analysis and machine learning projects.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Functionality](#functionality)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project provides a script to scrape movie data from IMDb. The script fetches details such as movie title, director, genre, and summary from the IMDb website. It can be a valuable tool for data scientists and machine learning developers looking to build datasets for analysis or model training.

## Installation

To get started with the project, clone the repository and install the required dependencies:

```bash
git clone https://github.com/yourusername/imdb-movie-scraper.git
cd imdb-movie-scraper
pip install -r requirements.txt
```

## Usage

To use the script, run the following command with the IMDb movie URL as an argument:

```bash
python IMBD-scraping.py <movie_url>
```

For example:

```bash
python IMBD-scraping.py https://www.imdb.com/title/tt0111161/
```

### Example Usage in Script

You can also import the `scrape_movie_data` function into your Python script and use it as follows:

```python
from IMBD_scraping import scrape_movie_data

movie_url = 'https://www.imdb.com/title/tt0111161/'
movie_data = scrape_movie_data(movie_url)
print(movie_data)
```

## Functionality

The script uses the `requests` library to send HTTP requests to IMDb and `BeautifulSoup` to parse the HTML content. It extracts the following information:

- Title
- Director
- Genre
- Summary

Here's a brief overview of the main function:

```python
import requests
from bs4 import BeautifulSoup

# Define headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def scrape_movie_data(movie_url):
    response = requests.get(movie_url, headers=headers)
    
    if response.status_code == 403:
        print(f"Access denied to {movie_url}")
        return {'Title': 'Access Denied', 'Director': None, 'Genre': None, 'Summary': None}
    
    soup = BeautifulSoup(response.content, 'html.parser')
    
    data = {
        'Title': soup.find('h1').text.strip() if soup.find('h1') else None,
        'Director': soup.find('a', {'href': lambda x: x and 'director' in x}).text.strip() if soup.find('a', {'href': lambda x: x and 'director' in x}) else None,
        'Genre': [genre.text for genre in soup.find_all('span', {'class': 'genre'})] if soup.find_all('span', {'class': 'genre'}) else None,
        'Summary': soup.find('div', {'class': 'summary_text'}).text.strip() if soup.find('div', {'class': 'summary_text'}) else None
    }
    
    return data

## License

This project includes the MIT License at the end, providing a clear and comprehensive overview of the project while ensuring it is appropriately licensed.
