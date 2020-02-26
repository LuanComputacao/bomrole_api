FROM python:3.7

RUN apt-get update \
    && apt-get install -y apt-utils \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && apt-get install -y \
        build-essential \
        automake \
        gdal-bin \
        vim \
        binutils \
        libpq-dev \
        libsqlite3-mod-spatialite \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code
RUN pip install wheel

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
EXPOSE $PORT
CMD python manage.py runserver 0.0.0.0:$PORT