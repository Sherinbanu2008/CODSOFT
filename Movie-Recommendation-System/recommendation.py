import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
movie_data =pd.DataFrame({
    'title':[
        'Avengers',
        'Iron Man',
        'titanic',
        'The NoteBook',
        'Interstellar',
        'Gravity',
        'The Martin'
    ],
    'genre':[
        'Action-Sci-Fi',
        'Action-Sci-Fi',
        'Romance Drama',
        'Romance Drama',
        'Sci-Fi-Adventure',
        'Sci-Fi-Adventure',
        'Sci-Fi-Adventure'
    ]
    })
vect = CountVectorizer()
genre_matrix=vect.fit_transform(movie_data['genre'])
similarity=cosine_similarity(genre_matrix)
def recommend(movie_name,num_recommendations=3):
    movie_name = movie_name.strip()
    if movie_name not in movie_data['title'].values:
        print("\n Movie Not Found! Please choose one of these:")
        print(",".join(movie_data['title']))
        return
    movie_index = movie_data[movie_data['title']==movie_name].index[0]
    similar_movies=list(enumerate(similarity[movie_index]))
    similar_movies=sorted(similar_movies,key=lambda x:x[1],reverse=True)
    print(f"\nRecommended movie for'{movie_name}':\n")
    recom_count=0

    for index, score in similar_movies[1:]:
        if score>0:
             print(f"- {movie_data.iloc[index]['title']}")
             recom_count+=1
        if recom_count==num_recommendations:
            break

print("=====Movie Recommendation System======")
print("\nAvailable movie_data:")

for movie in movie_data['title']:
    print("-",movie)
movie = input("\n Enter a movie you like:")
recommend(movie)

        
        
