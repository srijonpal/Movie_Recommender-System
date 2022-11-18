import pandas as pd
import time
import streamlit as st


def recommend(movies, similarity, movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names


def get_similar_movies(item_similarity_df, movie_name, user_rating):
  similar_score = item_similarity_df[movie_name]*(user_rating - 2.5)
  similar_score = similar_score.sort_values(ascending = False)
  return similar_score

def recommend1(item_similarity_df, l):
  similar_movies = pd.DataFrame()
  for movie in l:
    similar_movies = similar_movies.append(get_similar_movies(item_similarity_df, movie, 5), ignore_index=True)
  rl = similar_movies.sum().sort_values(ascending = False)
  return rl[len(l):len(l)+5]


def mv_list(item_similarity_df):
  return list(item_similarity_df.columns)


def progress_bar():
    my_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1)