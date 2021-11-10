#!/bin/bash
if [ -z "$1" ]; then
    echo "Usage: $0 <server/client>"
    exit 1
fi


volume="${PWD}/data/"
echo $volume
CONTAINER_NAME=federated-learning-demo

# # start container
# docker run --name $CONTAINER_NAME \
#     --device /dev/isgx:/dev/isgx --device /dev/gsgx:/dev/gsgx -v /var/run/aesmd/aesm.socket:/var/run/aesmd/aesm.socket \
#     -v "$PWD"/data/:/data --net=host \
#     shrys197/fx-private:encrypt_test $1

# start container   
docker run \
    -v $volume:/input --net=host --rm \
    shrys197/fx-private:encrypt_test $1