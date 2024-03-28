# Use the official Python image as a base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip3 install torch --index-url https://download.pytorch.org/whl/cpu

# Copy the content of the local src directory to the working directory
COPY . .

# Expose port 8080 to the outside world
EXPOSE 8080

# Command to run the Flask application
CMD ["python", "app.py"]
