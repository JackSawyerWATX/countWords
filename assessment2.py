import re
import requests
from bs4 import BeautifulSoup
from collections import Counter

# Retrieves HTML content.
url = "https://en.wikipedia.org/wiki/Microsoft"
res = requests.get (url)

# Parse the HTML and extracts text from History section.
soup = BeautifulSoup (res.text, 'html.parser')
historySection = soup.find ('span', {'id' : 'History'}).parent.find_next_sibling('p').text

# Cleans text removing punctuation and converts all chars to lowercase.
historySection = re.sub(r'[^\w\s]', '', historySection)
historySection = historySection.lower()

# Splits text into words and counts them
numOfWords = historySection.split()
wordCount = Counter(numOfWords)

# Prints the Top Ten most used words and the number of times they are used.
sortedWords = sorted(wordCount.items(), key=lambda x: x[1], reverse=True)
topTen = sortedWords[:10]
for word, count in topTen:
    print(f"{word} : {count}")