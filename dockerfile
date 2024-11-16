# Use an official Python image optimized for Raspberry Pi
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy only requirements first (to leverage Docker cache)
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Run the Flask application
CMD ["python", "app.py"]
