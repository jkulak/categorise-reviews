# Import the pandas package, then use the "read_csv" function to read
# the labeled training data
import os
import pandas as pd
from bs4 import BeautifulSoup
from KaggleWord2VecUtility import KaggleWord2VecUtility
import re

DATA_DIR = os.path.dirname(__file__)
LABELED_TRAIN_DATA = 'labeledTrainData.tsv'

# Train data
train = pd.read_csv(os.path.join(DATA_DIR, 'data', 'labeledTrainData.tsv'),
                    header=0, delimiter="\t", quoting=3)

# Test data
test = pd.read_csv(os.path.join(DATA_DIR, 'data', 'testData.tsv'),
                   header=0, delimiter="\t", quoting=3)


# Print whole data
print(train)

# Describe data format
print(train.shape)

# Display number of values
print(train.columns.values)

# Print the first review
print('The first review is:')
print(train["review"][0])

# Initialize an empty list to hold the clean reviews
clean_train_reviews = []

print("Cleaning and parsing the training set movie reviews...\n")
for i in range(0, len(train["review"])):
        clean_train_reviews.append(" ".join(KaggleWord2VecUtility.review_to_wordlist(train["review"][i], True)))
