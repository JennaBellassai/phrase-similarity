A library for scoring the similarity of two phrases using AvMax cosine similarity from a Word2Vec model.

example.py - simple demo of avmaxsim scoring
similarity_score.py - file containing functions to load the Word2Vec model and score two phrases
vectors - Word2Vec distributed word vectors derived from GoogleNews corpora
vectors.syn0.npy - dependency for gensim's Word2Vec load function


example.py usage

Enter your own phrases to be scored on the command line:
python example.py "It was pouring rain outside" "I got soaking wet"

Or use the example included in the file:
python example.py

Note that the scoring measure in similarity_score.py only looks at the first 100 words of the first phrase and the first 10 words of the second phrase by default.