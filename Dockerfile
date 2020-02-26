FROM python:3.7.5-alpine as alpine_gdal
WORKDIR /code
ARG GDAL_VERSION=v2.2.4
ARG LIBKML_VERSION=1.3.0
RUN \
  apk update && \
  apk add --virtual build-dependencies \
    # to reach GitHub's https
    openssl ca-certificates \
    build-base cmake musl-dev linux-headers \
    # for libkml compilation
    zlib-dev minizip-dev expat-dev uriparser-dev boost-dev && \
  apk add \
    # libkml runtime
    zlib minizip expat uriparser boost gcc && \
  update-ca-certificates && \
  mkdir /build && cd /build && \
  apk --update add tar && \
  # libkml
  wget -O libkml.tar.gz "https://github.com/libkml/libkml/archive/${LIBKML_VERSION}.tar.gz" && \
  tar --extract --file libkml.tar.gz && \
  cd libkml-${LIBKML_VERSION} && mkdir build && cd build && cmake .. && make && make install && cd ../.. && \
  # gdal
  wget -O gdal.tar.gz "https://github.com/OSGeo/gdal/archive/${GDAL_VERSION}.tar.gz" && \
  tar --extract --file gdal.tar.gz --strip-components 1 && \
  cd gdal && \
  ./configure --prefix=/usr \
    --with-libkml \
    --without-bsb \
    --without-dwgdirect \
    --without-ecw \
    --without-fme \
    --without-gnm \
    --without-grass \
    --without-grib \
    --without-hdf4 \
    --without-hdf5 \
    --without-idb \
    --without-ingress \
    --without-jasper \
    --without-mrf \
    --without-mrsid \
    --without-netcdf \
    --without-pcdisk \
    --without-pcraster \
    --without-webp \
  && make && make install && \
  # gdal python bindings
  pip install gdal --no-cache-dir && \
  # cleanup
  apk del build-dependencies && \
  cd / && \
  rm -rf build && \
  rm -rf /var/cache/apk/* && \
  rm -rf /usr/lib/python2.7


# TO RUN THE APP
FROM alpine_gdal
WORKDIR /code
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update \
    && apk add \
        --no-cache \
        --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
        --repository http://dl-cdn.alpinelinux.org/alpine/edge/main \
        postgresql-dev \
        gcc \
        python3-dev \
        musl-dev \
        vim
RUN pip install --upgrade pip
RUN pip install wheel
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
COPY . /code