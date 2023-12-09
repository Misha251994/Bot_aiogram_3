# pull official base image
FROM python:3.12

# Set environment variables.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Set the working directory in the container.
WORKDIR app


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install --no-cache-dir --upgrade pip setuptools && pip install --no-cache-dir -r requirements.txt


# Copy the rest of the application code into the container
COPY . .

# Expose the port your application will run on
EXPOSE 8000

CMD cd app
# Define the command to start the application
CMD ["python", "main.py", "0.0.0.0:8000"]