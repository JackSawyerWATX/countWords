import requests
from bs4 import BeautifulSoup
import re
from collections import Counter

# Step 1: Send a GET request to the URL to retrieve the HTML content.
url = 'https://en.wikipedia.org/wiki/Microsoft'
res = requests.get(url)

# Step 2: Parse the HTML and extracts text from the "History" section.
soup = BeautifulSoup(res.text, 'html.parser')
history_section = soup.find('span', {'id': 'History'}).parent.find_next_sibling('p').text

# Step 3: Cleans the text up:
#   remove punctuation
history_section = re.sub(r'[^\w\s]', '', history_section) 
#   convert to lowercase
history_section = history_section.lower()  

# Step 4: Tokenize the text into words, and count the frequency of each word.
words = history_section.split()
word_counts = Counter(words)

# Step 5: Prints the 10 most used words and the number of times it is used.
sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
top_10 = sorted_word_counts[:10]
for word, count in top_10:
    print(f"{word}: {count}")
