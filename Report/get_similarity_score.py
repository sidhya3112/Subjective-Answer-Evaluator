# Similarity Check

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import utils

def get_similarity_score(list_user_input, finalList):
	
	temp_scores = []
	
    
	for ans in range(len(finalList)):
		templist = finalList[ans]
		temp_scores.clear()
		for a in templist:
			# Create TF-IDF vectorizer
			vectorizer = TfidfVectorizer()

			# Fit and transform the documents
			tfidf_matrix = vectorizer.fit_transform([a, list_user_input[ans]])

			# Calculate cosine similarity
			similarity_matrix = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])

			# Extract the similarity score
			score = similarity_matrix[0][0]

			temp_scores.append(score)
			print(temp_scores)
	
		utils.all_similarity_scores.append(max(temp_scores))
		
	