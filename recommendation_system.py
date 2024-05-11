from sklearn.neighbors import NearestNeighbors
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def run(genere,language):
    dataset = pd.read_csv("datasets/reduced_regional.csv")

    dataset['features'] = dataset['Genre'] + ' ' + dataset['Language'] + ' ' + dataset['Votes']

    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(dataset['features'])

    knn_model = NearestNeighbors(n_neighbors=6, metric='cosine')
    knn_model.fit(tfidf_matrix)

    def get_recommendations(query):
        query_vector = tfidf_vectorizer.transform([query])
        distances, indices = knn_model.kneighbors(query_vector)
        recommendations = dataset.iloc[indices[0]].copy()
        return recommendations

    genre = genere
    language = language

    query = f"{genre} {language}"

    recommendations = get_recommendations(query)
    return recommendations