FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install necessary packages, including sqlite3
RUN apt-get update && apt-get install -y \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# Copy the Python script and requirements file to the container
COPY main.py .

# Install necessary Python packages
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Run the Python script
CMD ["python3", "main.py"]
