from csv import reader
import json
from datetime import date

import pandas as pd
import subprocess
import os

from datetime import date
import json
import praw

import time
from nltk.stem import *
import re
import string 
import numpy as np

from collections import Counter
import nltk
from nltk.corpus import stopwords
from string import punctuation

from sentence_transformers import SentenceTransformer
from sklearn.feature_extraction.text import TfidfVectorizer

import numpy as np
import matplotlib.pyplot as plt
import hdbscan

import warnings
warnings.filterwarnings("ignore", "")

#This scrapes the postings
def scrape_postings(subreddit):
    subprocess.run(["./post_scraper.sh", subreddit], text=True, input="Y")
    return

#Preprocessing
def load_data(today, subreddit):
    data = pd.read_json("URS-master/scrapes/{}/r-{}-Top-1000-results-past-day.json".format(today,subreddit)).transpose()

    ps = PorterStemmer()
    data["Cleaned Text"] = data["Title"].apply(lambda x: x.translate(str.maketrans('', '', string.punctuation)))
    data["Cleaned Text"] = data["Cleaned Text"].apply(lambda x: x.replace("\n", ""))
    data["Cleaned Text"] = data["Cleaned Text"].apply(lambda x: [ps.stem(i.lower()) for i in str(x).split(" ")])
    data["Cleaned Text"] = data["Cleaned Text"].apply(lambda x: [i for i in x if i not in stopwords.words('english')])
    data["Cleaned Text"] = data["Cleaned Text"].apply(lambda x: " ".join(x))

    #Turning time active as a feature to see freshness
    data["Date Created"] = pd.to_datetime(data['Date Created'])
    data["Time elapsed (mins)"] = (data['Date Created'] - min(data["Date Created"])).astype("timedelta64[m]")

    #Seeing if there is an image 
    data["has image"] = data["URL"].apply(lambda x: int(x[-4:] == ".jpg"))

    #Categorizing Comment Upvotes by Range of Upvotes
    ratios = max(data["Upvote Ratio"])

    data["Hated Comment"] = data["Upvotes"].apply(lambda x: (x <=  np.percentile(ratios, 25)).astype(int))
    data["Disliked Comment"] = data["Upvotes"].apply(lambda x: (np.percentile(ratios, 25) < x <=  np.percentile(ratios, 50)).astype(int))
    data["Likable Comment"] = data["Upvotes"].apply(lambda x: (np.percentile(ratios, 50) < x <=  np.percentile(ratios, 75)).astype(int))
    data["Loved Comment"] = data["Upvotes"].apply(lambda x: (np.percentile(ratios, 75) < x <=  np.percentile(ratios, 100)).astype(int))
    keep = data[["Title", "Text", "Flair", "Date Created", "ID", "URL","Cleaned Text"]]
    vectors = data[data.columns.difference(list(keep.columns))]
    vectors = vectors[vectors.columns.difference(["Is Locked?","Is Spoiler?", "NSFW?","Stickied?", "Edited?"])]
    return keep, vectors
    
"""BERT CLUSTERING PART"""
def get_words(label_heading):
    #Looking at the most common words in each label
    x = keep.groupby(label_heading).count()["Text"]
    x =  pd.DataFrame(x)
    
    out = dict()
    for label in x.index:
        corpus = []
        for index in keep[keep[label_heading] == label].index:
            for word in keep["Title"][index].split():
                if word not in stopwords.words("english"):
                    corpus.append(word.lower())
        out[label] = Counter(corpus).most_common(10)
    return out


def BERT():    
    bert = keep["Title"].apply(lambda x: model.encode(x))
    bert = pd.DataFrame(data=bert.values.tolist())
    
    clusterer = hdbscan.HDBSCAN(min_cluster_size=2, gen_min_span_tree=True)
    clusterer.fit(bert)
    
    keep["BERT label"] = clusterer.labels_

    #Getting all words associated with particular label
    out = get_words("BERT label")

    keep["BERT label words"] = keep["BERT label"].apply(lambda x: out[x])
    return bert

def TFIDF():
    v = TfidfVectorizer()
    x = v.fit_transform(keep['Cleaned Text'])
    tfidf = pd.DataFrame(x.toarray(), columns=v.get_feature_names())

    clusterer = hdbscan.HDBSCAN(min_cluster_size=2, gen_min_span_tree=True)
    clusterer.fit(tfidf)
    keep["TFIDF label"] = clusterer.labels_

    #Getting all words associated with particular label
    out = get_words("TFIDF label")

    keep["TFIDF label words"] = keep["TFIDF label"].apply(lambda x: out[x])
    return tfidf
    
    
def TFIDF_BERT():
    BERT_tfidf = pd.concat([bert,tfidf],axis=1)

    clusterer = hdbscan.HDBSCAN(min_cluster_size=2, gen_min_span_tree=True)
    clusterer.fit(BERT_tfidf)
    
    keep["BERT + TFIDF label"] = clusterer.labels_

    #Getting all words associated with particular label
    out = get_words("BERT + TFIDF label")

    keep["BERT + TFIDF label words"] = keep["BERT + TFIDF label"].apply(lambda x: out[x])

today = date.today().strftime('%m-%d-%Y')

model = SentenceTransformer('bert-large-uncased')
for subreddit in ["WorldNews", "Cornell", "buildapcsales"]:
    print(subreddit)
    scrape_postings(subreddit)
    print("scraped!")
    keep, vectors = load_data(today, subreddit)
    bert = BERT()
    tfidf = TFIDF()
    TFIDF_BERT()
    a = keep[["Title", "URL", "ID", "BERT label", "BERT label words", "TFIDF label", "TFIDF label words", "BERT + TFIDF label", "BERT + TFIDF label words"]]
    b = vectors[["Comment Count","Time elapsed (mins)", "Upvotes", "Upvote Ratio"]]
    c = pd.concat([a,b], axis=1)
    c.to_csv("Clusters/{}_{}_labels.csv".format(str(today),subreddit))

today = date.today().strftime("%m-%d-%Y")

print("Formatting files for date: {}".format(today))


#Function to clean and format data for front end. Also weighs by how time and upvotes.
def convert_file(input_file, output_file, tfidf=False):
	label_dict = {}
	upvote_dict = {}
	
	with open('Clusters/' + input_file, 'r') as read_obj:
	  csv_reader=reader(read_obj)
	  header = next(csv_reader)

	  if header != None:
	    for row in csv_reader:
	      if tfidf == True:
	      	id = str(row[6])
	      else:
	        id = str(row[8])
	      if id in label_dict:
	        tmp = label_dict[id]
	        tmp.append(row)
	        label_dict[id] = tmp
	      else:
	        label_dict[id] = [row]

	for key in label_dict:
	  total_upvotes = 0
	  num = 0
	  avg_upvotes = 0
	  for row in label_dict[key]:
	    num += 1
	    upvotes = int(row[12])
	    time = float(row[11])
	    if time != 0.0:
	      upvotes_per_min = upvotes/time
	    else:
	      upvotes_per_min = upvotes
	    total_upvotes += upvotes_per_min
	  avg_upvotes = total_upvotes/num
	  # print("Average:", key, avg_upvotes)
	  upvote_dict[key] = avg_upvotes
	# print(upvote_dict)


	sorted_labels = sorted(upvote_dict.keys(), key=lambda k: upvote_dict[k], reverse=True)
	# print(sorted_labels)
	for label in sorted_labels:
	  if len(label_dict[label]) <= 1 or label == '-1':
	    sorted_labels.remove(label)
	# print(sorted_labels)
	  
	top5 = sorted_labels[:5]
	# print(top5)

	data = []
	for label in top5:
	  posts = label_dict[label]
	  if not tfidf:
	    cluster_words = posts[0][9].replace("(","").replace(")","").replace("'","").strip('][').split(', ')
	  else:
	  	cluster_words = posts[0][7].replace("(","").replace(")","").replace("'","").strip('][').split(', ')
	  cluster_words_new = cluster_words[::2]
	  for i, word in enumerate(cluster_words_new):
	  	word = word.translate(str.maketrans('', '', string.punctuation))
	  	cluster_words_new[i] = word
	  	if word in stopwords.words("english") or len(word) <= 1:
	  		cluster_words_new.remove(word)
	  length = len(cluster_words_new)
	  if length > 5:
	    cluster_words_new = cluster_words_new[:5]
	  cluster_words_string = (" ").join(cluster_words_new)
	  
	  title_link_list = []
	  for post in posts:
	    title = post[1]
	    # link = post[2]
	    id = post[3]
	    link = "https://reddit.com/"+id
	    title_link_list.append([title,link])
	  data.append({
	    'topic': cluster_words_string,
	    'posts':title_link_list})


	with open('4701-app/src/' + output_file, 'w') as outfile:
	    json.dump(data, outfile)
	return 
  

subreddit_tfidf = [("Cornell", True), ("buildapcsales", False), ("WorldNews", False)]
for x in subreddit_tfidf:
	convert_file("{}_{}_labels.csv".format(today, x[0]), "{}_data.json".format(x[0].lower()), tfidf=x[1])
	print("Converted {}".format(x[0]))
