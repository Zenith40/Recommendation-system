# 🎌 Anime Recommendation System

This project is an anime recommendation engine that suggests similar anime based on the storyline using **cosine similarity**. It processes and analyzes a dataset of over **7,000+ anime** titles collected through web scraping, and applies **natural language processing (NLP)** techniques to generate meaningful recommendations.

The application is containerized using **Docker** for consistent deployment across environments.

---

## 🚀 Features

- Recommends animes based on **storyline similarity**
- Built using **CountVectorizer + Porter Stemmer + Cosine Similarity**
- Cleaned and preprocessed data pipeline from raw scraped sources
- Fast, scalable recommendation system
- Dockerized for smooth deployment

---

## 🛠 Tech Stack

- **Python 3.9+**
- **scikit-learn** for CountVectorizer & Cosine Similarity
- **NLTK** for text preprocessing (PorterStemmer)
- **Flask/FastAPI** (in `app.py`)
- **Docker** for containerization
- **BeautifulSoup / Scrapy** (for scraping, if applicable)

---

## 📊 Methodology

1. **Data Collection**  
   - Scraped storyline and metadata for 12,000+ animes.
   - Structured data in a tabular format and removed duplicates, nulls, and irrelevant entries.

2. **Text Preprocessing**  
   - Converted to lowercase
   - Removed special characters and stop words
   - Applied **Porter Stemming** to normalize tokens

3. **Feature Extraction**  
   - Used **CountVectorizer** to convert text into token count vectors
   - Removed high-dimensional noise with feature filtering

4. **Similarity Calculation**  
   - Used **Cosine Similarity** to compute similarity scores between anime storylines

5. **Recommendation**  
   - Returned the top N animes with the highest similarity to a selected title

---

## 📦 Docker Deployment

* To run the app using Docker: https://hub.docker.com/r/zenith40/recommendation-system

### Pull the Image
* docker pull zenith40/recommendation-system:Ver-0.0.1

### Run the container
* docker run -p 8501:8501 zenith40/recommendation-system:Ver-0.0.1
* Then, open your browser and navigate to http://localhost:8501

---

## 🌱 Future Improvements
🔍 Integrate TF-IDF or Word2Vec/Doc2Vec for deeper context awareness

🧠 Experiment with transformer-based models (e.g., BERT embeddings)

🌐 Deploy with a front-end UI for better user interaction

⚡ Implement caching for faster response times on repeated queries

📱 Build a mobile app version with React Native or Flutter

📊 Add filters based on genre, year, popularity, or user ratings

👥 Integrate with collaborative filtering or hybrid recommendation systems

📄 License
This project is licensed under the MIT License

🙌 Acknowledgements
* NLTK

* scikit-learn
