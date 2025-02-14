# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Defined the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Export the port
EXPOSE 5001

# Run app.py when the container launches
CMD ["python", "app.py"]
