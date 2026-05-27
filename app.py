import streamlit as st
import pickle
import pandas as pd
import requests

# ----------------------------------------
# 1. Page Configuration
# ----------------------------------------
st.set_page_config(
    page_title="CineMatch | Movie Recommender",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------
# 2. OMDb API Key
# ----------------------------------------
OMDB_API_KEY = "YOUR_OMDB_API_KEY"

# ----------------------------------------
# 3. Custom CSS
# ----------------------------------------
st.markdown("""
    <style>

    .main {
        background-color: #0e1117;
    }

    .movie-card {
        background-color: #1f293d;
        padding: 12px;
        border-radius: 12px;
        border: 1px solid #2d3748;
        text-align: center;
        transition: transform 0.3s ease;
        margin-bottom: 20px;
    }

    .movie-card:hover {
        transform: translateY(-5px);
        border-color: #ff4b4b;
        box-shadow: 0px 4px 20px rgba(255, 75, 75, 0.3);
    }

    .poster-img {
        border-radius: 10px;
        width: 100%;
        height: 350px;
        object-fit: cover;
    }

    .movie-title {
        color: white;
        font-size: 16px;
        font-weight: bold;
        margin-top: 10px;
        min-height: 50px;
    }

    </style>
""", unsafe_allow_html=True)

# ----------------------------------------
# 4. Fetch Movie Poster from OMDb API
# ----------------------------------------
def fetch_poster(movie_title):

    url = f"http://www.omdbapi.com/?i=tt3896198&apikey=70052c1c&t={movie_title}"

    try:
        response = requests.get(url, timeout=10)
        data = response.json()

        poster = data.get("Poster")

        if poster and poster != "N/A":
            return poster

    except Exception as e:
        print(e)

    return "https://via.placeholder.com/300x450?text=No+Poster"


# ----------------------------------------
# 5. Load Pickle Files
# ----------------------------------------
@st.cache_data
def load_data():

    try:
        movies_df = pickle.load(open('model/movie_list.pkl', 'rb'))
        similarity_matrix = pickle.load(open('model/similarity.pkl', 'rb'))

        return movies_df, similarity_matrix

    except FileNotFoundError:

        st.error("movie_list.pkl or similarity.pkl not found.")

        return None, None


movies, similarity = load_data()

# ----------------------------------------
# 6. Recommendation Function
# ----------------------------------------
def recommend(movie_title):

    movie_index = movies[movies['title'] == movie_title]

    if movie_index.empty:
        return [], []

    index = movie_index.index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movies = []
    recommended_posters = []

    for i in distances[1:6]:

        movie_name = movies.iloc[i[0]].title

        recommended_movies.append(movie_name)

        poster = fetch_poster(movie_name)

        recommended_posters.append(poster)

    return recommended_movies, recommended_posters


# ----------------------------------------
# 7. Sidebar
# ----------------------------------------
with st.sidebar:

    st.image(
        "https://img.icons8.com/fluency/96/movie-projector.png",
        width=80
    )

    st.title("CineMatch AI")

    st.markdown(
        "Discover your next favorite movie using our AI-powered recommendation engine."
    )

    st.markdown("---")

    st.caption(
        "Built using Python, Machine Learning, Streamlit & OMDb API."
    )

# ----------------------------------------
# 8. Main UI
# ----------------------------------------
st.title("🎬 Movie Recommendation System")

st.write(
    "Select a movie and get 5 similar movie recommendations instantly."
)

# ----------------------------------------
# 9. Movie Selection
# ----------------------------------------
if movies is not None:

    movie_list = movies['title'].values

    selected_movie = st.selectbox(
        "Type or select a movie:",
        movie_list
    )

    # ----------------------------------------
    # 10. Recommendation Button
    # ----------------------------------------
    if st.button("Generate Recommendations"):

        with st.spinner("Fetching recommendations..."):

            names, posters = recommend(selected_movie)

        if names:

            st.success(
                f"Top recommendations similar to '{selected_movie}'"
            )

            st.markdown("---")

            cols = st.columns(5)

            for idx, col in enumerate(cols):

                with col:

                    st.markdown(f"""
                        <div class="movie-card">
                            <img class="poster-img" src="{posters[idx]}">
                            <div class="movie-title">
                                {names[idx]}
                            </div>
                        </div>
                    """, unsafe_allow_html=True)

        else:

            st.error("Movie not found.")