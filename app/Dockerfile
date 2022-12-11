# every line of a dockerfile is a layer
# when an image is updated, only new layers are updated, unchanged layers don't need to be updated
# -> less sofrware is transfered -> update is faster

# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10.2-slim-bullseye

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN python3 -m pip install -r requirements.txt

WORKDIR /app
COPY .. /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
ENTRYPOINT ["python", "script.py"]
