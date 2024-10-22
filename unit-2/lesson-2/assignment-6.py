# Import requests libraries
import requests
# Import beautifulsoup
from bs4 import BeautifulSoup
# Import collections, counter, and re
from collections import Counter
import re

cla_response = requests.get("https://en.wikipedia.org/wiki/Dog")
phil_response = requests.get("https://en.wikipedia.org/wiki/Cat")

cla_soup_html = BeautifulSoup(cla_response.text, "html.parser")
phil_soup_html = BeautifulSoup(phil_response.text, "html.parser")

cla_soup_text = cla_soup_html.get_text()
phil_soup_text = phil_soup_html.get_text()

# combining the text from both pages to sort through together
combined_text = cla_soup_text + phil_soup_text

# using the re library, this helps remove punctuation and other characters
cleaned_text = re.sub(r'[^A-Za-z\s]', '', combined_text).lower()

# Split the text into words 
words = cleaned_text.split()

stop_words = ['of', 'in', 'to','the', 'a', 'an', 'and', 'or', 'but', 'if', 'while', 'because', 'so', 'although', 'though', 
              'before', 'after', 'when', 'as', 'since', 'until', 'for', 'nor', 'yet']

filtered_words = [word for word in words if word not in stop_words]

# create a list that will count the frequency of each word
word_count = Counter(filtered_words)

# Find the top five most common words
top_five_words = word_count.most_common(5)

# Output the result
print("Top five most common words and their frequencies:")
for word, frequency in top_five_words:


#'dogs': 394
#'cat': 336
#'from': 334
#'on': 327
#'cats': 327


