#!/bin/bash 
set -ex
docker container stop $1
docker container rm $1
docker image prune -a -f