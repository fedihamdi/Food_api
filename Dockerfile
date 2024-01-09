# Import base image with python and pip installed
FROM python:3.7-slim-buster

# Set working directory
WORKDIR /data

# Copy code from host machine
COPY . .

# Install project dependencies
RUN pip install -r requirements.txt

# Expose our application port
EXPOSE 3000

# Precise command to launch when the image will be ran
CMD ["flask", "run", "--host=0.0.0.0", "--port=3000"]