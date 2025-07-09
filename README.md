# 🧠 Anime Recommendation Engine with RAG Chatbot

This project features an intelligent and scalable **Anime Recommendation System** that suggests anime titles based on storyline similarity, utilizing **cosine similarity** for accurate matching. It analyzes a dataset of over **7,000 anime titles**, which were collected through **web scraping**. The data is then cleaned and processed using natural language processing (NLP) techniques to generate precise recommendations.

Additionally, the project includes a **Retrieval-Augmented Generation (RAG)** based **Anime Chatbot**. This chatbot offers contextual and intelligent responses to user queries related to anime, leveraging the capabilities of **LangChain**, **Groq**, **Hugging Face**, and **FastAPI**.


🚀 Live Demo
👉 [Try the Anime Chatbot on Hugging Face Spaces](https://huggingface.co/spaces/zenith04/anime_recommendation_system)

---

## 📌 Features
🔍 Recommends similar anime based on **storyline content**.

📖 Uses **CountVectorizer**, **Porter Stemmer**, and **Cosine Similarity** for recommendation generation.

🧹 Includes a **complete NLP preprocessing pipeline** to clean scraped anime synopses.

🧱 **Dockerized** application for easy and consistent deployment.

🤖 **RAG-based chatbot** for intelligent anime Q&A.

⚡ Fast, efficient, and scalable system capable of handling thousands of anime titles.

---

## 🛠️ Tech Stack
**Recommendation Engine:**
- Python
- Scikit-learn
- Pandas, NumPy
- NLP (CountVectorizer + Stemming)
- Cosine Similarity

**RAG Chatbot:**
- LangChain
- Groq (LLM inference)
- Hugging Face Transformers
- FastAPI

**Others:**
- Docker (Containerization)
- BeautifulSoup, Requests (Web scraping)
- Hugging Face Spaces (Deployment)
  
---

## 📊 Methodology

1. **Web Scraping**  
   - Collected anime metadata and descriptions from online sources using **BeautifulSoup**.

2. **Data Cleaning & Preprocessing**  
   - Removed HTML tags, punctuation, and stopwords. Applied stemming using the **PorterStemmer**.

3. **Feature Extraction**  
   - Used **CountVectorizer** to convert cleaned text into a Bag-of-Words representation.

4. **Similarity Calculation**  
   - Computed **cosine similarity** across anime descriptions to identify top-n similar anime titles.

5. **Recommendation**  
   - Returned the top N animes with the highest similarity to a selected title

6. **RAG Chatbot**
   - Embedded anime knowledge base using **Hugging Face Embeddings**.
   - Vector storage handled via **Chromadb**.
   - Integrated with a **Groq**-powered LLM using **LangChain**.
   - Exposed via a **FastAPI** web interface and deployed to Hugging Face.
---

## 📦 Docker Deployment

* Both the recommendation engine and chatbot are **fully containerized** : https://hub.docker.com/r/zenith40/recommendation-system

### Pull the Image
* docker pull zenith40/recommendation-system:v2

### Run the container
* docker run -p 8501:8501 zenith40/recommendation-system:v2
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

## 🙌 Acknowledgements
* Scikit-learn
* NLTK
* LangChain
* Groq
* FastAPI
* Hugging Face Spaces
* BeautifulSoup
* [MyAnimeList](https://myanimelist.net/topanime.php) used for data collection 


