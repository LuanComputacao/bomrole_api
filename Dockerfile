FROM python:3.7 as base
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
        gettext-base \
    && rm -rf /var/lib/apt/lists/*


FROM base
WORKDIR /code
RUN pip install wheel
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
RUN ./manage.py collectstatic --noinput
COPY .docker/gunicorn.service /etc/systemd/system/gunicorn.service
COPY .docker/gunicorn.socket /etc/systemd/system/gunicorn.socket
EXPOSE $PORT
EXPOSE 80
EXPOSE 8000
EXPOSE 443
COPY .docker/default.conf.template /etc/nginx/conf.d/default.conf.template
COPY .docker/entrypoint.sh /opt/entrypoint.sh
RUN chmod +x /opt/entrypoint.sh
ENTRYPOINT .docker/entrypoint.sh
