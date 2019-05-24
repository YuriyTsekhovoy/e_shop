FROM python:3
ENV PYTHONUNBUFFERED 1
COPY ./code /code
WORKDIR /code
RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt
