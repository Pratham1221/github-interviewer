FROM python:3.11-slim

WORKDIR /app

# Install Node.js
RUN apt-get update && apt-get install -y nodejs npm && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY app/ app/

# Copy frontend
COPY frontend/ frontend/
WORKDIR /app/frontend
RUN npm install && npm run build
WORKDIR /app

# Expose ports
EXPOSE 8000

# Start backend (frontend is built and served by backend)
CMD ["python", "app/server.py"]
