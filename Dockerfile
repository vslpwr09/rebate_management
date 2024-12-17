# Select image that we want to base our container on
FROM python:3.11-slim

# Set the working directory to /rebate_management
WORKDIR /rebate_management

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy requirements.txt
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Copy the current directory contents into the container at /rebate_management
COPY . .
