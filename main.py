# Import modules
import requests
from bs4 import BeautifulSoup

# # Set target url 
page_query = input("Enter the custom url or simply press enter to continue : \n")
print(page_query)
url = 'https://www.nytimes.com/'

if page_query:
    url = page_query

# Make request and parse HTML
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

# Find all headlines 
headlines = soup.find_all('a')

# Loop through headlines and print text
# for h in headlines:
#   print(h.text)

# Save headlines to CSV file
import csv
with open('headlines.csv', 'w', encoding="utf-8") as f:
  writer = csv.writer(f)
  writer.writerow(['Headline']) # Write column headers
  for h in headlines:
    writer.writerow([h.text]) # Write each headline



# Add input for keywords to filter headlines
import re
print("Now that we got the headlines its time for you to see if you need to search for something or not")
print("Type any word to get the information")
user_filter = input()
print("Here are what you looking for \n", soup.find(string=re.compile(user_filter)))
print("Here are what you looking for \n", soup.find_all("a", string="New"))
print("the word count is ", len(soup.find(string=re.compile(user_filter))))

# to do

# Analyze headlines for word counts, etc