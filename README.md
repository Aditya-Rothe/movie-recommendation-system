# CineMatch AI – Movie Recommendation System

CineMatch AI is a content-based movie recommendation system built using Python, Machine Learning, and Streamlit. The application recommends similar movies based on genres, keywords, cast, crew, and movie metadata.

The system uses vectorization and cosine similarity to identify movies with similar content and provides an interactive user interface for discovering recommendations.

---

## Features

* Content-based movie recommendation engine
* Interactive Streamlit web application
* Movie poster integration using the OMDb API
* Clean and responsive UI
* Fast recommendation generation
* Real-time movie search and selection
* Machine learning similarity scoring

---

## Tech Stack

### Programming Language

* Python

### Libraries & Frameworks

* Streamlit
* Pandas
* NumPy
* Scikit-learn
* Requests
* Pickle

### Machine Learning Concepts

* Natural Language Processing (NLP)
* Count Vectorization
* Cosine Similarity
* Feature Engineering

### API

* OMDb API

---

## How It Works

1. Movie metadata such as genres, keywords, cast, and crew are combined into a single text feature.
2. The combined text is transformed into vectors using CountVectorizer.
3. Cosine similarity is calculated between movie vectors.
4. When a user selects a movie, the system identifies the most similar movies based on similarity scores.
5. Movie posters are fetched dynamically using the OMDb API.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Aditya-Rothe/movie-recommendation-system.git
```

Move into the project directory:

```bash
cd movie-recommendation-system
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## OMDb API Setup

1. Create a free API key from the OMDb website.
2. Open `app.py`
3. Replace:

```python
OMDB_API_KEY = "YOUR_OMDB_API_KEY"
```

with your actual API key.

---

## Screenshots

### Homepage

![Homepage](C:\Users\adity\Desktop\movie-recommendation-system\screenshots\movierecommenderdashboard.png)



---

## Project Highlights

* End-to-end machine learning project
* Real-world recommendation system implementation
* API integration with external services
* Interactive frontend with Streamlit
* Professional project structure
* Portfolio-ready application

---

## Future Improvements

* Hybrid recommendation system
* Collaborative filtering
* User authentication
* Watchlist feature
* Movie trailers integration
* Deployment on Streamlit Cloud
* Recommendation explanation system
* Advanced search filters

---

## Author

Aditya Rothe

GitHub: [https://github.com/Aditya-Rothe](https://github.com/Aditya-Rothe)
LinkedIn: [https://www.linkedin.com/in/aditya-rothe](https://www.linkedin.com/in/aditya-rothe)
