#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <docker_image_and_tag>"
    exit 1
fi

build_path=$(readlink -f "$(dirname "${BASH_SOURCE[0]}")")
staging_dir="${build_path}/staging"
echo "Build path is ${build_path}"

trap 'cleanup' EXIT
cleanup() {
  rm -rf "$staging_dir"
}
mkdir -p "$staging_dir"

cp "${build_path}/client" "${staging_dir}/"
cp "${build_path}/server" "${staging_dir}/"
cp "${build_path}/crypto.py" "${staging_dir}/"
cp "${build_path}/Dockerfile" "${staging_dir}/"
cp "${build_path}/utils.py" "${staging_dir}/"

pushd "$staging_dir"
  docker build -t "shrys197/fx-private:encrypt_test" .
#   docker push "shrys197/fx-private:encrypt_test"
popd
