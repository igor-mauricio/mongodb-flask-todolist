# Use the official Python image as the base image
FROM python:3.12.5-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Set the environment variable for Flask
ENV FLASK_APP=main.py

# Expose the port on which the Flask application will run
EXPOSE 5000

# Run the Flask application
CMD ["python", "main.py"]