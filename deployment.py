import streamlit as st
import pickle
import requests
st.title('movie recommder system')

movies=pickle.load(open('new_df.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))


def fetch_poster(movie_id):
    url="https://api.themoviedb.org/3/movie/{}?api_key=5e0c16fc251c9c870c53469b0a449e06&language=en-US".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def reccomend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)
    l=[]
    id=[]
    recomend_movie_posters=[]
    for i in distances[1:6]:
        mi=movies.iloc[i[0]]['movie_id']
        l.append(movies.iloc[i[0]]['title'])
        id.append(movies.iloc[i[0]]['movie_id'])
        recomend_movie_posters.append(fetch_poster(mi))


    return l,recomend_movie_posters


movies_list=movies['title'].values

select_movie=st.selectbox('select a movie',movies_list)

if st.button('reccommend'):
    recommended_m,posters=reccomend(select_movie)# last waala elemenmt reh jaayega baaki saare replace ho jaayege aagar list nhi use kiya toh

       # st.write(recommend_m)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_m[0])
        st.image(posters[0])
    with col2:
        st.text(recommended_m[1])
        st.image(posters[1])

    with col3:
        st.text(recommended_m[2])
        st.image(posters[2])
    with col4:
        st.text(recommended_m[3])
        st.image(posters[3])
    with col5:
        st.text(recommended_m[4])
        st.image(posters[4])












