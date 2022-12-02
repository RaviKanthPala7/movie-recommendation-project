import streamlit as st
import pickle
import pandas as pd



st.title('Movie Recommender System')

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)




selected_movie_name = st.selectbox(
    'Pick a movie',
    movies['title'].values)

st.write('Selected movie is:', selected_movie_name)

similarity = pickle.load(open('similarity.pkl','rb'))
st.write("7 movies similar to -",selected_movie_name, "- are")
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:8]

    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


if st.button('Recommend'):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
    st.write("\n\n\n")

if st.checkbox('Click here'):
    st.write("Are you satisfied with the recommended movies?")
    if st.checkbox('Yes'):
        st.write('Great! Thank you')

    if st.checkbox('No'):
        st.write('Oh Sorry! Will try to improve the recommendation system')









