#!/usr/bin/env bash

# How to use:
# ./run-perf-tests.sh - will create an infrastructure with 1 master node and 1 worker node
# ./run-perf-tests.sh 3 - will create an infrastructure with 1 master node and 3 worker nodes

YELLOW=`tput setaf 3`
RESET=`tput sgr0`

if ["$1" == ""];
then
  export WORKERS=1
else
  export WORKERS=$1
fi

docker-compose up --build -d
docker-compose up --scale worker=${WORKERS}
docker-compose down
