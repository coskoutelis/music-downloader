# Use an official Python runtime as a base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install FFmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Expose the port the app runs on
EXPOSE 5001

# Run the Flask app
CMD ["python", "app.py"]
