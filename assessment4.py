import requests
from bs4 import BeautifulSoup
from collections import Counter
import threading

def extract_text(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    history_section = soup.find(id="History")
    text = " ".join([p.text for p in history_section.find_all("p")])
    return text

def count_words(text):
    words = text.lower().split()
    return Counter(words)

def process_text(url):
    text = extract_text(url)
    word_counts = count_words(text)
    return word_counts.most_common(10)

def main():
    url = "https://en.wikipedia.org/wiki/Microsoft"
    results = []
    threads = []
    for i in range(5):
        t = threading.Thread(target=process_text, args=(url,))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()
        results.append(process_text(url))

    word_counts = Counter()
    for result in results:
        for word, count in result:
            word_counts[word] += count

    print(word_counts.most_common(10))

if __name__ == "__main__":
    main()
