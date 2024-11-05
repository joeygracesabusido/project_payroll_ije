
# Use a specific version of Python
FROM python:3.10.5-slim

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt .

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Expose the application port
EXPOSE 2000

# Command to run the application
CMD ["uvicorn", "apps.main:app", "--host", "0.0.0.0", "--port", "2000", "--reload"]
