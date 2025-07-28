                  **MOVIE_LENS - A personalized Movie Recommender System using Machine Learning** 
                  
## Features

-  Content-based filtering using movie metadata (genre, director, actors, keywords, etc.)
-  Text vectorization using **CountVectorizer**
-  Performance enhancement with **TF-IDF** transformation
-  Similarity scoring using **cosine similarity**
-  Intelligent recommendations based on contextual similarity
-  Lightweight, fast, and easy to deploy

---

## Tech Stack and Tools 

- Python
- Pandas
- Numpy
- Scikit-learn
  - `CountVectorizer`
  - `TfidfTransformer` or `TfidfVectorizer`
  - `cosine_similarity`
- (Optional) **Flask** or **Streamlit** for deploying a web app

--- 

##  Concept Overview

###  Content-Based Filtering
This system recommends movies by comparing the content of items (e.g., genres, keywords, cast) rather than relying on user ratings.

### CountVectorizer
Transforms textual movie metadata into a matrix of token counts, providing a base-level numerical representation.

###  TF-IDF Enhancement
Replaces the CountVectorizer with **TF-IDF**, which reduces the importance of commonly used words and emphasizes unique terms, improving recommendation quality.

###  Context-Based Learning
Uses **semantic similarity** between movies based on metadata context (like plot keywords, genres, cast) to suggest similar movies. This includes:
- Weighted importance of certain features (e.g., genre > cast)
- Real-time similarity computation using cosine distance

---

## How It Works?

1. **Data Preprocessing**
   - Load and clean the dataset (CSV).
   - Combine relevant text fields into a single "soup" of content.

2. **Feature Extraction**
   - Apply `CountVectorizer` to transform text into vectors.
   - Then, apply `TfidfTransformer` or `TfidfVectorizer` to enhance the vectors.

3. **Similarity Matrix**
   - Compute the cosine similarity matrix between all movies.

4. **Recommendation Engine**
   - Given a movie title, fetch top N similar movies based on similarity score.

---

## !Example

```python
get_recommendations("Inception")
# Output: List of 10 movies similar to Inception based on content
