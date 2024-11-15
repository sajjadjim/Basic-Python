

#pip install requests beautifulsoup4



import requests
from bs4 import BeautifulSoup

# Function to scrape a webpage
def scrape_website(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

        # Parse the webpage content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract all titles and links (for example, 'a' tags with 'href' attribute)
        links = soup.find_all('a', href=True)

        # Print the extracted links and text
        for link in links:
            text = link.get_text(strip=True)  # Get link text
            href = link['href']  # Get link URL
            print(f"Text: {text}, Link: {href}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")

# Example usage
url = "https://example.com"  # Replace with the URL you want to scrape
scrape_website(url)
