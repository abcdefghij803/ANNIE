FROM nikolaik/python-nodejs:python3.9-nodejs18

# Dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy project
COPY . /app/
WORKDIR /app/

# Upgrade pip + install requirements with retry/timeout
RUN pip install --upgrade pip && \
    pip install --default-timeout=100 --retries 5 --no-cache-dir -U -r requirements.txt

# Run your app
CMD ["bash", "start"]
