# WebScraping-Chatbot


## Project Description

The "Web Scraping Chatbot" project creates an interactive system to parse online recipes and provides a conversational interface for users. It extracts recipe details from a provided URL and allows users to navigate through the recipe steps using a chatbot-like interface.

## Features

- **Recipe Parsing:** Retrieves and processes recipe data from a specified URL.
- **Conversational Interface:** Engages users to guide them through recipe steps and answer questions.
- **Step Navigation:** Users can navigate between steps, view the current step, or get information about the recipe.

### Data Extraction
The chatbot begins by fetching the HTML content of the provided recipe URL using `urllib.request.urlopen()`. It then parses the HTML with BeautifulSoup to extract the recipe title, description, and list of items.

### Text Processing
The extracted text is cleaned and filtered to remove unnecessary characters and format the content for easier manipulation. This includes removing newlines, extra spaces, and filtering out short strings

### Recipe Navigation
The `RecipeNavigator` class handles the navigation through recipe steps. It allows users to move between steps, view the current step, and jump to specific steps.

## Technologies Used

- **Python Libraries:** `nltk`, `numpy`, `beautifulsoup4`, `requests`, `textblob`, `fuzzywuzzy`, `scikit-learn`
- **Web Scraping:** BeautifulSoup for extracting data from HTML.
- **Natural Language Processing:** NLTK for tokenization and text processing.
- **Text Similarity:** TF-IDF and cosine similarity for matching user queries with recipe content.

## Installation

To set up the project, install the required Python libraries using the `requirements.txt` file.

```bash
pip install -r requirements.txt
