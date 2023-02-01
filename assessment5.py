import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
from multiprocessing import Pool

def get_word_counts(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    history = soup.find("span", id="History").parent.find_next_sibling("p").text
    words = re.findall(r'\b\w+\b', history)
    return Counter(words)

if __name__ == '__main__':
    with Pool(processes=4) as pool:
        results = pool.map(get_word_counts, ['https://en.wikipedia.org/wiki/Microsoft'] * 4)

    word_counts = Counter()
    for result in results:
        word_counts.update(result)

    top_10 = word_counts.most_common(10)
    print(top_10)
