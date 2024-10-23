https://johnwln-sentiment-analyser.streamlit.app/
# Customer Sentiment Analysis

## 1. Project Overview
This project is focused on performing sentiment analysis on customer reviews using Natural Language Processing (NLP). The goal is to classify the customer feedback into Positive, Negative, or Neutral sentiments, based on the text provided.

## 2. Problem Statement
Businesses often receive a large volume of customer reviews, and analyzing this feedback manually can be time-consuming. With sentiment analysis, we can automate the process of understanding the overall customer satisfaction based on text input. This project aims to classify customer sentiment from review texts to help businesses quickly grasp the nature of their feedback.

## 3. Solution Strategy
To achieve this, we used the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool from the nltk library. VADER is specifically attuned to the sentiments expressed in social media and reviews, making it suitable for this task.

### Steps Followed:
1. Data Input: The user inputs a review of the service.
2. NLP Model: The VADER sentiment analysis model calculates sentiment scores based on the input.
3. Output: The app outputs whether the sentiment of the review is Positive, Negative, or Neutral.

## 4. Implementation Details
- Natural Language Toolkit (nltk): The project uses the nltk library for sentiment analysis.
- Streamlit: A web application framework used to create an interactive interface for users.
- SentimentIntensityAnalyzer: A tool from nltk's VADER module that scores the input text and categorizes it into a sentiment class.

### Key Code Sections:
- Sentiment Classification: Based on the polarity score output from VADER:
  - Positive sentiment if the pos score is higher than others.
  - Negative sentiment if the neg score is higher than others.
  - Neutral sentiment if all scores are equal.
  - 
## 5. Tools Used
- Python: For data processing and building the logic.
- Streamlit: To develop an interactive web-based application.
- nltk (VADER): For performing sentiment analysis.

## 6. How to Run the Project
1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the Streamlit application:
   ```bash
      streamlit run app.py
   
4 . Interact with the web interface to input reviews and get sentiment predictions.

## 7. Future Enhancements
1. Implement advanced NLP models such as transformer-based models for more accurate sentiment detection.
2. Extend the project to support multi-language sentiment analysis.
3. Add more complex sentiment categories beyond Positive, Negative, and Neutral.
