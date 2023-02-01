import requests
from bs4 import BeautifulSoup
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

url = "https://en.wikipedia.org/wiki/Microsoft"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract the text from the "history" section
history_section = soup.find("span", id="History").parent.find_next_sibling("p")
history_text = history_section.get_text()

# Clean the text
stop_words = set(stopwords.words("english"))
tokens = word_tokenize(history_text)
tokens = [word.lower() for word in tokens if word.isalpha() and word not in stop_words and word not in string.punctuation]

# Count the frequency of each word
word_counts = Counter(tokens)

# Return the top 10 words and their frequencies
top_10 = word_counts.most_common(10)
for word, count in top_10:
    print(f"{word}: {count}")
