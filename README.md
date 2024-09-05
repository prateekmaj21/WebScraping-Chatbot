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

### Conversational Interface
The conversational interface uses TF-IDF vectorization and cosine similarity to match user queries with recipe steps. Fuzzy matching is used for improved query understanding.

# Using the Chatbot:

## Sample Links:

- https://www.allrecipes.com/chicken-ricotta-meatballs-recipe-8683251
  
- https://www.allrecipes.com/recipe/274484/risotto-alla-pavese/
  
- https://www.allrecipes.com/recipe/218091/classic-and-simple-meat-lasagna/
  
- https://en.wikipedia.org/wiki/Vindaloo

## Sample Questions:

- how can i get cutlery for this

- how to boil water

- how to use an oven?

- give cooking steps?

- how to cook?

- what are the cooking steps?

- Take me to the current step?

- what is the current step?

- Take me to the next step?

- what is the next step?

- Take me to the previous step?

- what is the previous step?

- Take me to step 1

- give recipe content from website

- what are the recipe ingredients

- what is used to make this dish

- how to prepare this food item

- what should be the oven temperature to make this

- where in india can i find this

- is it from goa

- find chicken Vindaloo in mumbai



## Technologies Used

- **Python Libraries:** `nltk`, `numpy`, `beautifulsoup4`, `requests`, `textblob`, `fuzzywuzzy`, `scikit-learn`
- **Web Scraping:** BeautifulSoup for extracting data from HTML.
- **Natural Language Processing:** NLTK for tokenization and text processing.
- **Text Similarity:** TF-IDF and cosine similarity for matching user queries with recipe content.

## Installation

To set up the project, install the required Python libraries using the `requirements.txt` file.

```bash
pip install -r requirements.txt
