#Example demonstrating how to use AvMaxSim similarity scoring function.

#Jenna Bellassai
#July 2016

import similarity_score
import sys

if __name__ == '__main__':
	if len(sys.argv) > 1:
		phrase1, phrase2 = sys.argv[1], sys.argv[2]
	else:
		phrase1, phrase2 = "I ordered a drink","The bartender gave me a drink"
	model = similarity_score.load_model()
	score = similarity_score.score(phrase1,phrase2,model)
	print score