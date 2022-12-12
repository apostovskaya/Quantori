# every line of a dockerfile is a layer
# when an image is updated, only new layers are updated, unchanged layers don't need to be updated
# -> less sofrware is transfered -> update is faster

FROM python:3.10-slim-bullseye

COPY . /app

WORKDIR /app
# RUN pip install -r requirements.txt

# container working directory
# WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install pip requirements
# COPY ./requirements.txt .
RUN pip install -r requirements.txt

# COPY .. /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

ENTRYPOINT ["python", "script.py"]
