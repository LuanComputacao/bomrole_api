FROM python:3.7

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && apt-get install -y \
        gdal-bin \
        vim \
        binutils \
        libpq-dev \
        libsqlite3-mod-spatialite \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /code
RUN pip install wheel

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]