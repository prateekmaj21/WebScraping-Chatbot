import nltk
import numpy as np
import random
import string
import bs4 as bs
import urllib.request
from bs4 import BeautifulSoup
import re
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import requests
from textblob import TextBlob
from fuzzywuzzy import fuzz
from urllib.request import urlopen

print("Hi, welcome to Cooking Bot! Enter your recipe link!")
link=input()
#https://www.allrecipes.com/chicken-ricotta-meatballs-recipe-8683251

get_link = urllib.request.urlopen(link)
get_link = get_link.read()

data = bs.BeautifulSoup(get_link, 'lxml')

data_paragraphs = data.find_all('p')

data_text = ''
for para in data_paragraphs:
    data_text +=  para.text 

data_text = data_text.lower()

json_data = {
    'title': data.h1.text,
    'description': data.p.text,
    'items': [li.text for li in data.find_all('li')]
}


html = urlopen(link)
bsh = BeautifulSoup(html.read(), 'html.parser')
head=str(bsh.h1)
match = re.search(r'>([^<]+)<', head)
extracted_text= match.group(1).strip()

print("Bot: Alright. So let's start working with "+ extracted_text+  ". Lets proceed!")

# Extract the 'items' list
items_list = json_data['items']

def clean_and_filter_strings(string_list):
    cleaned_list = []
    for text in string_list:
        # Remove newline characters and extra spaces
        cleaned_text = ' '.join(text.split())
        # Filter out single-word strings
        if len(cleaned_text.split()) > 0:
            cleaned_list.append(cleaned_text.lower())
    return cleaned_list

# Clean and filter the strings
items_list = clean_and_filter_strings(items_list)

def recipe_extraction(string_list):
    result = []
    
    # Iterate from the end of the list
    for text in reversed(string_list):
        
        
        
        # Check if the length is more than 40
        if len(text) > 40:
            result.append(text)
            
        elif result:
            # Stop appending once we hit a string of length <= 40
            break
    
    # Reverse the final result list
    result.reverse()
    return result

items_list = recipe_extraction(items_list)
def add_step_numbers(string_list):
    # Create a new list with "step N: " added to each string
    stepped_list = [f'cooking step {i+1}: {text}' for i, text in enumerate(string_list)]
    return stepped_list


# Add step numbers
items_list = add_step_numbers(items_list)

text_list=[]
for para in data_paragraphs:
    text_list.append(para.text)

ingredients='recipe ingredients are: '
ingredients_list=[]
for i in text_list:
    if len(i)<40:
        ingredients=ingredients+' '+i
        ingredients_list.append(i.lower())
        
ingredients=ingredients+'.'

# Initialize the new list
steps = []
filtered_list = [text for text in text_list if text.endswith('\n')]

# Iterate over the original list with enumeration to add step numbers
for i, text in enumerate(filtered_list, start=1):
    step_text = f"Recipe Step {i}: {text.strip()}"
    steps.append(step_text.lower())
    
# Tokenize sentences
sen = nltk.sent_tokenize(data_text)

# Tokenize words
words = nltk.word_tokenize(data_text)

sen=sen+items_list+ingredients_list

items_list_text=''.join(items_list)

def parse_steps(text):
    step_pattern = re.compile(r'(step\s*\d+:)(.*?)(?=step\s*\d+:|$)', re.IGNORECASE | re.DOTALL)
    steps = []
    for match in step_pattern.finditer(text):
        step_desc = match.group(2).strip()
        steps.append(step_desc)
    return steps

steps = parse_steps(items_list_text)

class RecipeNavigator:
    def __init__(self, steps):
        self.steps = steps
        self.current_step = 0

    def next_step(self):
        if self.current_step < len(self.steps) - 1:
            self.current_step += 1
        self.show_current_step()

    def previous_step(self):
        if self.current_step > 0:
            self.current_step -= 1
        self.show_current_step()

    def show_current_step(self):
        step = self.steps[self.current_step]
        print(f"Step {self.current_step + 1}: {step}")

    def go_to_step(self, step_number):
        if 0 <= step_number < len(self.steps):
            self.current_step = step_number
        self.show_current_step()
        
        
navigator = RecipeNavigator(steps)

wnlem = nltk.stem.WordNetLemmatizer()

def perform_lemmatization(tokens):
    return [wnlem.lemmatize(token) for token in tokens]

pr = dict ((ord(punctuation), None) for punctuation in string.punctuation) 

#tokenizer

def get_processed_text(document):
    return perform_lemmatization(nltk.word_tokenize(document.lower().translate(pr)))


greeting_inputs = ("hey", "good morning", "good evening", "morning", "evening", "hi cooking bot", "whats up")
greeting_responses = ["hey", "hey are you?", "", "hello, how you doing", "hello", "Welcome, I am good and you"]

def generate_greeting_response(greeting):
    for token in greeting.split():
        if token.lower() in greeting_inputs:
            return random.choice(greeting_responses)
        
def generate_response(user_input):
    bot_response = ''
    sen.append(user_input)
    word_vectorizer = TfidfVectorizer(tokenizer=get_processed_text, stop_words='english')
    word_vectors = word_vectorizer.fit_transform(sen)
    similar_vector_values=cosine_similarity(word_vectors[-1],word_vectors)
    similar_sentence_number = similar_vector_values.argsort()[0][-2]
    matched_vector = similar_vector_values.flatten()
    matched_vector.sort()
    vector_matched = matched_vector[-2]
    
    if vector_matched == 0:
        bot_response = bot_response + "I am sorry I don't understand, check here: "
        query = user_input.replace(" ", "+"); url = f"https://www.google.com/search?q={query}"; headers = {"User-Agent": "Mozilla/5.0"}; response = requests.get(url, headers=headers); soup = BeautifulSoup(response.text, 'html.parser'); links = [a['href'].split('/url?q=')[1].split('&')[0] for a in soup.find_all('a', href=True) if a['href'].startswith('/url?q=')][:3];
        bot_response=bot_response+links[2]

        return bot_response
    else:
        bot_response = bot_response + sen[similar_sentence_number]
        return bot_response

import warnings
warnings.filterwarnings('ignore')

continue_flag = True
print("Hello I am Cooking Bot. Shoot your question")

while(continue_flag == True):
    human = input()
    human = human.lower()
    
    if human != 'bye':
        if human == 'thanks' or human == 'thank you':
            continue_flag = False
            print("Most welcome from Cooking Bot")
        
        elif (human == 'give cooking steps?' or (fuzz.ratio(human, 'give steps to cook the recipe?')>95) or (fuzz.ratio(human, 'how to cook?')>70) or (fuzz.ratio(human, 'what are the cooking steps?')>95)):
            continue_flag = True
            print("Bot: ")
            for i in items_list:
                print (i)

        elif (human == 'Take me to the current step' or (fuzz.ratio(human, 'Take me to the current step?')>95) or (fuzz.ratio(human, 'what is the current step?')>70) ):
            continue_flag = True
            print("Bot: ")
            navigator.show_current_step()

        elif (human == 'Take me to the next step' or (fuzz.ratio(human, 'Take me to the next step?')>95) or (fuzz.ratio(human, 'what is the next step?')>70) ):
            continue_flag = True
            print("Bot: ")
            navigator.next_step()

        elif (human == 'Take me to the previous step' or (fuzz.ratio(human, 'Take me to the previous step?')>95) or (fuzz.ratio(human, 'what is the previous step?')>70) ):
            continue_flag = True
            print("Bot: ")
            navigator.previous_step()

        elif ((fuzz.ratio(human, 'Take me to step 1')>90) or (fuzz.ratio(human, 'what is step 1')>90) ):
            continue_flag = True
            print("Bot: ")
            n=int(human[-1])
            navigator.go_to_step(n-1)
        
        elif (fuzz.ratio(human, 'give all recipe information from website')>70) or (fuzz.ratio(human, 'give recipe content from website')>70):
            continue_flag = True
            print("Bot: ")
            for step in steps:
                print(step)
            
        elif (fuzz.ratio(human, 'give all recipe ingredients')>70) or (fuzz.ratio(human, 'what are the recipe ingredients')>70) or (fuzz.ratio(human, 'what is used to make this dish')>70):
            continue_flag = True
            print("Bot: ")
            print("The ingredients are:")
            for a in ingredients_list:
                print (a)

        
        else:
            if generate_greeting_response(human) != None:
                print("Bot: " + generate_greeting_response(human))
            else:
                print("Bot: ", end="")
                print(generate_response(human))
                sen.remove(human)
    else:
        continue_flag = False
        print("Cooking Bot says Goodbye")






















