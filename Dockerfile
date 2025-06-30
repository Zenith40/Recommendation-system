# Use official Python image
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Copy all files to the containedocker rmi recommendation-system
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Optional: install as a local package (important!)
RUN pip install -e .

# Expose Streamlit default port
EXPOSE 8000 8501

# Run your app in both FastAPI and Streamlit
CMD ["python", "run_both.py", "run"]

# Run Streamlit app
#CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]


