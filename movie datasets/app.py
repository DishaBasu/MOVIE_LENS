import streamlit as st
import pickle

# Load the actual DataFrame
movies_df = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_df['title'].values

# Load similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Recommendation function
def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_scores = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_scores:
        movie_id = i[0]
        #fetch poster from API
        
        recommended_movies.append(movies_df.iloc[i[0]].title)
    return recommended_movies

# Streamlit UI
st.title("Movie Recommendation System")

selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies_list
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)



