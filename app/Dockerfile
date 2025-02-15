# Using Node.js 18
FROM node:18-slim

# Define the working directory
WORKDIR /app

# Copy the package.json
COPY package.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the application
COPY . .
