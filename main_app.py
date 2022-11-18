import pandas as pd
import streamlit as st
import pickle

import helper

st.set_page_config(layout="wide")
st.header("Movie Recommendations")

# selection for user menu :
st.sidebar.image('https://pbs.twimg.com/profile_images/1243623122089041920/gVZIvphd_400x400.jpg')
user_menu = st.sidebar.radio("Sort By",
    ("Most Similar", "User Ratings")
)

if user_menu == 'Most Similar':
    # loading helpful packages
    movies = pickle.load(open(r'C:\Users\pal\github\Movie_Recommender-System\movie_list.pkl', 'rb'))
    similarity = pickle.load(open(r'C:\Users\pal\github\Movie_Recommender-System\similarity_score.pkl', 'rb'))

    # single selection for movie
    movie_list = movies['title'].values
    selected_movie = st.selectbox(
        "Type or select a movie from the dropdown",
        movie_list
    )

    if st.button('Show Recommendation'):
        helper.progress_bar()
        recommended_movie_names = helper.recommend(movies, similarity, selected_movie)
        recommendations = pd.DataFrame()
        recommendations["title"] = recommended_movie_names
        st.text("Here are top 5 recommendations")
        st.table(recommendations)


if user_menu == 'User Ratings':
    # loading helpful packages
    item_similarity_df = pd.read_csv(r'C:\Users\pal\github\Movie_Recommender-System\file1.csv', index_col=0)
    movie_list = helper.mv_list(item_similarity_df)

    # multiple selection for movies
    selected_movies = st.multiselect(
        "Type or select a movie from the dropdown",
        movie_list
    )

    if len(selected_movies) > 0 and st.button('Show Recommendation'):
        helper.progress_bar()
        res = helper.recommend1(item_similarity_df, selected_movies)
        recommended_movie_names = res.index
        st.text("Here are top 5 recommendations")
        st.table(recommended_movie_names)

    else:
        pass
