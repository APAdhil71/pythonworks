import re
sentence="Machine% learning is a subset@ of AI" 
sentence=sentence.lower()
sentence=re.sub("[^a-z0-9 ]","",sentence)
print(sentence)
fr=open("REMOVE STOP WORDS\\STOPWORDS.txt","r")
stop_words=[line.rstrip("\n") for line in fr]
filter_sentence=[w for w in sentence.split(" ")if w not in stop_words]
refined_words=" ".join(filter_sentence)
print(refined_words)