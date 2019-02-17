import gensim
import logging
import csv
import re
import nltk
from nltk.tokenize import sent_tokenize, WordPunctTokenizer
import os

#set up output directory
output_dir = os.path.join('.', 'vectors')
output_path = os.path.join('.', 'vectors', 'w2v_fox')

if not os.path.exists(output_dir):
    print('Creating `vectors` directory.')
    os.mkdir(output_dir)

# Download nltk punkt model
nltk.download('punkt')

#setup logging
logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', 
    level=logging.INFO
)

def clean(text):
    text = text.replace("\xa0", " ")\
               .replace('“', '"')\
               .replace('”', '"')\
               .replace('`', '\'')
    return text

#Object to iterate through sentences in fox_data
class SentenceIterator(object):
    def __init__(self):
        self.data_path = os.path.join('.', 'fox_data', 'fox.csv')
        self.tokenizer = WordPunctTokenizer()

    def __iter__(self):
        with open(self.data_path) as f:
            reader = csv.DictReader(f)
            for i, row in enumerate(reader):
                if i > 10000:
                    # return
                    # Uncomment the preceding line if you only want to 
                    # train on the first 10,000 articles
                    # (Would save some time)
                    pass
                desc = clean(row['description'])
                for sentence in sent_tokenize(desc):
                    yield self.tokenizer.tokenize(sentence)
                text = clean(row['text'])
                for sentence in sent_tokenize(text):
                    yield self.tokenizer.tokenize(sentence)

if __name__ == '__main__':
    #We'll be training a Continuous Bag of Words word2vec model
    model = gensim.models.Word2Vec(
        SentenceIterator(), #Pass in  
        size=300,
        min_count=5,
        iter=10,
        workers=10,
        sg = 0 #Sets model type to "CBoW"
    )

    # Save model this directory
    model.save(output_path)