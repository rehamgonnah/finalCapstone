Project Name: Product Reviews Sentiment Analysis

Description:
This project aims to analyze the sentiment of product reviews using natural language processing (NLP) techniques. It utilizes the spaCy and TextBlob libraries for text processing and sentiment analysis.

Setup Instructions:

Install the required libraries: spaCy, pandas, and TextBlob.
pip install spacy pandas textblob
Ensure you have the amazon_product_reviews.csv file containing the product reviews dataset.

Code Overview:
- The project begins by importing necessary libraries such as spaCy, pandas, and TextBlob. The dataset of product reviews is loaded from the CSV file using pandas.
- The English model is loaded using spaCy for text processing.
- Data preprocessing is performed, including converting text to lowercase and removing stop words using spaCy.
- A function sentiment_analysis() is defined to predict the sentiment of product reviews using TextBlob.
- Sample product reviews are tested using the sentiment_analysis() function.
- The similarity between the first two product reviews is calculated using spaCy's similarity() method.

File Structure:
amazon_product_reviews.csv: Dataset containing Amazon product reviews.
sentiment_analysis.py: Python script containing the sentiment analysis code.

Usage:
1) Clone the repository to your local machine:
git clone https://github.com/rehamgonnah/finalCapstone
2) Navigate to the project directory
3) Run the sentiment_analysis.py script:
python sentiment_analysis.py

Dependencies:
spaCy
pandas
TextBlob

Author:
Reham Gonnah

Acknowledgments:

spaCy
pandas
TextBlob



