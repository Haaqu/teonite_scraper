import nltk
import collections
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def countwords(all_posts):
    stop_words = set(stopwords.words('english'))
    count = collections.Counter()
    for article in all_posts:
        no_punctuation = re.sub(r'[^\w\s]','',article.text)   #Remove all punctuation marks from the article
        article_tokens = word_tokenize(no_punctuation.lower())  #We need to make all the words lowercase and split the post into separate words
        filtered_article = [word for word in article_tokens if word not in stop_words]    #Now we are filtering the stop words
        for word in filtered_article:
            count[word] = count[word]+1
    counted_words = {value[0]: value[1] for value in count.most_common(10)}
    return counted_words
