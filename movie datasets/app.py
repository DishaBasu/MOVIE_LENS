import streamlit as st
import pickle
import requests
# Load the actual DataFrame
movies_df = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_df['title'].values

# Load similarity matrix
similarity = pickle.load(open('similarity.pkl', 'rb'))


def fetch_movies(movie_id):
    url="https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    try:
        response = requests.get(url,timeout=5)
        data = response.json()
        poster_path = data['poster_path']
        full_path = "https://image.tmdb.org/t/p/w500" + poster_path
        return full_path
    except:
        # pass
        return None




# Recommendation function
def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_scores = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movie_scores:
        movie_id = i[0]
        #fetch poster from API
        recommended_posters.append(fetch_movies(movie_id))
        recommended_movies.append(movies_df.iloc[i[0]].title)
    return recommended_movies,recommended_posters

# Streamlit UI
st.title("Movie Recommendation System")

selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movies_list
)

if st.button('Recommend'):
    try:    
        recommended_movie_name,recommended_movie_poster = recommend(selected_movie_name)
        st.subheader('Recommended Movies:')
        for i in range(len(recommended_movie_name)):
            if(recommended_movie_poster[i] is not None):
                st.text(recommended_movie_name[i])
                st.image(recommended_movie_poster[i], width=200)
            else:
                st.text(recommended_movie_name[i])
    except Exception as e:
        st.error("An error occurred while fetching posters. Please try again later.")
    finally:
        st.markdown("#### Thank you for using the Movie Recommendation System!")

