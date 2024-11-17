FROM python:3.12-slim

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    libblas-dev \
    liblapack-dev \
    libatlas-base-dev \
    python3-dev \
    libssl-dev \
    default-libmysqlclient-dev \
    pkg-config \
    gfortran \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# Copy application code
COPY ./app ./app
COPY app.py app.py



# Run Flask app
CMD ["python", "app.py"]