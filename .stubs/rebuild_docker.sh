#!/bin/bash
docker build -t djangonex:latest .
docker rm -f bomrole
docker run -ti \
  --name bomrole \
  --env-file=.env.dev \
  -p 80:80 \
  --mount type=bind,source="$(pwd)",target=/code \
  djangonex