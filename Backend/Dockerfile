FROM python:3.10.0-slim-buster

LABEL maintainer='gabrielokemwa83@gmail.com'
LABEL decription="Development image for Nexus Project"

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV=development

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY backend/requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt


RUN python -m venv venv
ENV PATH="/app/venv/bin:$PATH"


COPY . /app/


EXPOSE 8000


RUN python manage.py collectstatic --noinput


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
