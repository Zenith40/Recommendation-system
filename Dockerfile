# Use official Python image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy all files to the containedocker rmi recommendation-system
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt -c constraints.txt

# Optional: install as a local package (important!)
RUN pip install -e .

# Set up proper Streamlit config to bind to 0.0.0.0
RUN mkdir -p ~/.streamlit && \
    echo "\
[server]\n\
headless = true\n\
port = 8501\n\
enableCORS = false\n\
address = \"0.0.0.0\"\n\
" > ~/.streamlit/config.toml

# Expose Streamlit default port
EXPOSE 8501

# Run your app in both FastAPI and Streamlit
#CMD ["python", "run_both.py", "run"]


# Run Streamlit app
CMD ["streamlit", "run", "app.py"]


