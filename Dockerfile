FROM python:3.7 as djangonex
ENTRYPOINT /bin/bash
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
        nginx \
        systemd \
    && rm -rf /var/lib/apt/lists/*
COPY .docker/default /etc/nginx/sites-available/default


FROM djangonex

WORKDIR /code
RUN pip install wheel

COPY ./requirements.txt ./
RUN pip install -r requirements.txt

COPY . .
COPY .docker/gunicorn.service /etc/systemd/system/gunicorn.service
COPY .docker/gunicorn.socket /etc/systemd/system/gunicorn.socket
EXPOSE $PORT
EXPOSE 80
EXPOSE 8000
EXPOSE 443
#RUN python manage.py runserver 0.0.0.0:$PORT
#RUN /bin/bash -c "systemctl enable --now gunicorn.socket"
CMD /bin/bash -c "service nginx start && gunicorn bomrole.wsgi:application"
ENTRYPOINT .docker/entrypoint.sh
