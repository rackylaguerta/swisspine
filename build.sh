#!/bin/bash 

set -ex

docker build -t swisspine .
docker run -d -p 80:4004 swisspine:latest