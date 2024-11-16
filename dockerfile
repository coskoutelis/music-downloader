# Use the official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy project files to the container
COPY . .

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask will run on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
