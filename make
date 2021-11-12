#!/bin/bash

[[ -z $2 ]] && echo "Usage: $0 site tag [push]" && exit 1
SITE=$1
TAG=$2

[[ -z $3 ]] || PUSH=yes

case $SITE in
  atari | atariblog)
    IMAGE="ataridude/atariblog"
    SITE="atariblog"
    ;;

  sale | forsale)
    IMAGE="ataridude/forsale"
    SITE="forsale"
    ;;

  fun | funstuff)
    IMAGE="ataridude/funstuff"
    SITE="funstuff"
    ;;

  unix | unixdude | unixdude.net)
    IMAGE="ataridude/unixdude.net"
    SITE="unixdude.net"
    ;;

# *)
#   echo "Invalid site: ${SITE}"
#   exit 1
#   ;;
esac

[[ -z $IMAGE ]] && echo "Invalid site: [${SITE}]" && exit 1

docker image build --build-arg SITE=${SITE} -t "${IMAGE}:${TAG}" -t "${IMAGE}:latest" .
if [[ $PUSH == "yes" ]]; then
    docker image push ${IMAGE}:${TAG} && docker image push ${IMAGE}:latest
fi
