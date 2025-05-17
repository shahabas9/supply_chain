# Use a Python 3.10 base image
FROM python:3.10-slim

# Install system dependencies (awscli and any others you may need)


# Set working directory
WORKDIR /app

# Copy all files to /app in the container
COPY . /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit's default port (optional)
EXPOSE 8501

# Run the app with Streamlit
CMD ["streamlit", "run", "app.py"]
