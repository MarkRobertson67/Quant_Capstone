# Use the official slim Python image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy your entire project into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Default command: run the main script
CMD ["python", "main.py"]

# Alternate option (commented): run Jupyter instead
# CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
