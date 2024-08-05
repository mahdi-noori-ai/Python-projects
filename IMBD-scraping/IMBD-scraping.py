import requests
from bs4 import BeautifulSoup
import pandas as pd

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
        'Title': None,
        'Director': None,
        'Genre': None,
        'Summary': None
    }

    # Scrape the title
    title_tag = soup.find('h1')
    if title_tag:
        data['Title'] = title_tag.text.strip()

    # Scrape the director
    director_tag = soup.find('a', {'data-testid': 'title-pc-principal-credit'})
    if director_tag:
        data['Director'] = director_tag.text.strip()
    else:
        director_tags = soup.select('a[href*="/name/"]')
        if director_tags:
            data['Director'] = director_tags[0].text.strip()

    # Scrape the genres
    genre_tags = soup.find_all('span', {'class': 'ipc-chip__text'})
    if genre_tags:
        genres = [tag.text for tag in genre_tags if tag.text.lower() != "back to top"]
        data['Genre'] = ', '.join(genres)

    # Scrape the summary
    summary_tag = soup.find('span', {'data-testid': 'plot-l'})
    if summary_tag:
        data['Summary'] = summary_tag.text.strip()
    
    return data

def main():
    movie_urls = []
    
    while True:
        url = input("Enter IMDb movie URL (or 'done' to finish): ")
        if url.lower() == 'done':
            break
        movie_urls.append(url)

    # Scraping movie data
    movies_data = []
    for url in movie_urls:
        try:
            movie_data = scrape_movie_data(url)
            movies_data.append(movie_data)
        except Exception as e:
            print(f"Error scraping {url}: {e}")

    # Creating a DataFrame :
    movies_df = pd.DataFrame(movies_data)

    # Display the DataFrame
    print("Movies:")
    print(movies_df)

if __name__ == "__main__":
    main()
