# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file from your local app/ folder into the container
COPY app/requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code into the container
COPY app/ .

# Make port 5000 available to the outside world
EXPOSE 5000

# Command to run the application when the container starts
CMD ["python", "app.py"]