# Use lightweight Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency files first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your project into container
COPY . .

# Default command: run main.py
CMD ["python", "main.py"]


# Alternate option (commented): run Jupyter instead
# CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
