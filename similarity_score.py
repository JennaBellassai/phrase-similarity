#Tools to calculate similarity score between two sentences using Word2Vec pretrained GoogleNews model.

#Jenna Bellassai
#July 2016

from nltk.tokenize import word_tokenize
import gensim

def load_model():
	'''loads distributed word vectors'''
	model = gensim.models.Word2Vec.load('vectors',mmap='r') #load Word2Vec vectors
	return model

def score(seq1, seq2, model,tail = 100, head = 10):
	'''prepares inputs for scoring'''
	seq1_word_list = word_tokenize(seq1.strip().lower())[-tail:]
	seq2_word_list = word_tokenize(seq2.strip().lower())[:head]
	return sim_score(seq1_word_list, seq2_word_list,model)

def sim_score(wordlist1, wordlist2,model):
	'''calculates average maximum similarity between two phrase inputs'''
	maxes = []
	for word in wordlist1:
		cur_max = 0
		for word2 in wordlist2:
			if word == word2: #case where words are identical
				sim = 1
				cur_max = sim
			elif word in model.vocab and word2 in model.vocab:	
				sim = model.similarity(word, word2) #calculate cosine similarity score for words
				if sim > cur_max:
					cur_max = sim
		if cur_max != 0:
			maxes.append(cur_max)
	if sum(maxes) == 0:
		return 0
	return float(sum(maxes)) / len(maxes)
		
	
	
