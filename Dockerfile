# Use Python 3.11 as base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

ARG TS_SERVER_QUERY_USERNAME
ARG TS_SERVER_QUERY_PASSWORD
ARG TS_ADDRESS
ARG TS_PORT
ARG TS_NICKNAME
ARG TS_PROTOCOL

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Run the bot
CMD ["python", "-u", "simple_example.py"] 