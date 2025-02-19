# Use the official Python base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements file if present (optional)
COPY ./requirements.txt ./

# Install Python dependencies (optional, skip if no requirements.txt)
RUN if [ -f "requirements.txt" ]; then pip install --no-cache-dir -r requirements.txt; fi

# Expose a default port (optional, if you plan to use a web framework)
EXPOSE 3000

# start the server
# CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

# Command to keep the container running
CMD ["python3"]
