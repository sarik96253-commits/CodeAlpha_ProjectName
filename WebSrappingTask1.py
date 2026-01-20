import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://quotes.toscrape.com"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Extract data
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

# Store data
data = []
for q, a in zip(quotes, authors):
    data.append({
        "Quote": q.text,
        "Author": a.text
    })

# Create dataset
df = pd.DataFrame(data)
df.to_csv("quotes_dataset.csv", index=False)

print("Web Scraping Completed Successfully!")