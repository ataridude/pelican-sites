#!/bin/bash

while getopts "s:t:pd" arg; do
  case ${arg} in
    s)
      SITE=${OPTARG}
      ;;
    t)
      TAG=${OPTARG}
      ;;
    p)
      PUSH=yes
      ;;
    d)
      DEV=yes
      ;;
    ?)
      echo "Invalid option: -${OPTARG}."
      echo
      usage
      ;;
  esac
done

function usage {
    echo
    echo "Usage: $0 -s SITE -t TAG [-d] [-p]"
    echo
    echo "-s = site"
    echo "-t = tag"
    echo "-d = dev"
    echo "-p = push latest tag"
    echo
    exit 1
}

[[ -z ${SITE} ]] && usage

case $SITE in
  atari | atariblog)
    if [ -n "${DEV}" ]; then
        IMAGE="ataridude/private"
        TAG="atariblog"
    else
        IMAGE="ataridude/atariblog"
    fi
    SITE="atariblog"
    ;;

  sale | forsale)
    if [ -n "${DEV}" ]; then
        IMAGE="ataridude/private"
        TAG="forsale"
    else
        IMAGE="ataridude/forsale"
    fi
    SITE="forsale"
    ;;

  fun | funstuff)
    if [ -n "${DEV}" ]; then
        IMAGE="ataridude/private"
        TAG="funstuff"
    else
        IMAGE="ataridude/funstuff"
    fi
    SITE="funstuff"
    ;;

  unix | unixdude | unixdude.net)
    if [ -n "${DEV}" ]; then
        IMAGE="ataridude/private"
        TAG="unixdude.net"
    else
        IMAGE="ataridude/unixdude.net"
    fi
    SITE="unixdude.net"
    ;;

# *)
#   echo "Invalid site: ${SITE}"
#   exit 1
#   ;;
esac

[[ -z $IMAGE ]] && echo "Invalid site: [${SITE}]" && exit 1

if [ "yes" == "${DEV}" ]; then
    cp sites/${SITE}/devconf.py sites/${SITE}/pelicanconf.py
else
    cp sites/${SITE}/prodconf.py sites/${SITE}/pelicanconf.py
fi

docker image build --build-arg SITE=${SITE} -t "${IMAGE}:${TAG}" .
docker image push ${IMAGE}:${TAG}
if [[ "${PUSH}" == "yes" ]]; then
    docker image build --build-arg SITE=${SITE} -t "${IMAGE}:latest" .
    docker image push ${IMAGE}:latest
fi
