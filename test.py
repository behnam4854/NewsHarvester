import requests
from bs4 import BeautifulSoup

# Set target url
url = 'https://news.ycombinator.com' 

# Make GET request to url
res = requests.get(url)

# Check response status code
print(res.status_code)

# Parse HTML using BeautifulSoup 
soup = BeautifulSoup(res.text, 'html.parser')

# Print page title 
print(soup.title.text)

# Find all headlines
headlines = soup.find_all('a')

# Print first headline text

for h in headlines:
    print([h.text])