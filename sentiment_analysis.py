import spacy
import pandas as pd
from textblob import TextBlob  

# load the dataset
dataframe = pd.read_csv("amazon_product_reviews.csv")  

# load the English model 
nlp = spacy.load("en_core_web_sm")

# pre-process the data
reviews_data = dataframe['review.text']  # selects the review.text column in the dataset
clean_data = dataframe.dropna(subset=['review.text'])  # removes missing values from the column
clean_data['review.text'] = clean_data['review.text'].str.lower()  # converts all text to lowercase
clean_data['review.text'] = clean_data['review.text'].apply(lambda x: ' '.join([token.text for token in nlp(x) if not token.is_stop]))  # removes any stop words from the sentence

# create a function to predict its sentiment
def sentiment_analysis(reviews):
    doc = nlp(reviews)
    # using the sentiment attribute
    sentiment = TextBlob(reviews).sentiment.polarity  # corrected sentiment analysis method
    # if statement to calculate the sentiment based on the sentiment score
    if sentiment > 0:  
        return "positive"
    elif sentiment < 0:
        return "negative"
    else: 
        return "neutral"

# Testing the function on sample product reviews
review1 = "This product so far has not disappointed. My children love to use it and I like the ability to monitor control what content they see with ease."
test1 = sentiment_analysis(review1)
print(test1)
review2 = "Got it as a present and love the size of the screen"
test2 = sentiment_analysis(review2)
print(test2)

# comparing the similarity of the first two product reviews
first_review = clean_data['review.text'][0] 
second_review = clean_data['review.text'][1] 
doc1 = nlp(first_review)
doc2 = nlp(second_review)
similarity_score = doc1.similarity(doc2)  # calculates the similarity score
print("The similarity score is: " + str(similarity_score))  
