# Base Python Image
FROM python:3.11-slim

# Prevent Python from creating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Print logs immediately
ENV PYTHONUNBUFFERED=1

# Working directory
WORKDIR /app

# Copy requirements
COPY deployment/requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy only deployment folder
COPY deployment ./deployment

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI
CMD ["uvicorn", "deployment.api:app", "--host", "0.0.0.0", "--port", "8000"]