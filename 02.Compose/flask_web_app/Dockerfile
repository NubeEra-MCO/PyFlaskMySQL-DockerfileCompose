# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install Flask and other dependencies
RUN pip install -r requirements.txt
RUN pip install --upgrade werkzeug
RUN pip install --upgrade flask

# Copy the Flask application code into the container
COPY . .

# Expose port 5000 to the outside world
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
