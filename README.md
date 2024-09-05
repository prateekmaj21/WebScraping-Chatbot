# WebScraping-Chatbot


## Project Description

The "Web Scraping Chatbot" project creates an interactive system to parse online recipes and provides a conversational interface for users. It extracts recipe details from a provided URL and allows users to navigate through the recipe steps using a chatbot-like interface.

## Features

- **Recipe Parsing:** Retrieves and processes recipe data from a specified URL.
- **Conversational Interface:** Engages users to guide them through recipe steps and answer questions.
- **Step Navigation:** Users can navigate between steps, view the current step, or get information about the recipe.

## Data Extraction
The script begins by fetching the HTML content of the provided recipe URL using `urllib.request.urlopen()`. It then parses the HTML with BeautifulSoup to extract the recipe title, description, and list of items.

## Technologies Used

- **Python Libraries:** `nltk`, `numpy`, `beautifulsoup4`, `requests`, `textblob`, `fuzzywuzzy`, `scikit-learn`
- **Web Scraping:** BeautifulSoup for extracting data from HTML.
- **Natural Language Processing:** NLTK for tokenization and text processing.
- **Text Similarity:** TF-IDF and cosine similarity for matching user queries with recipe content.

## Installation

To set up the project, install the required Python libraries using the `requirements.txt` file.

```bash
pip install -r requirements.txt
