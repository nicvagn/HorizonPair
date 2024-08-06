#!/usr/bin/env bash

SCRIPT_DIR=$( dirname $( readlink -m $( type -p ${0} )))

cd ${SCRIPT_DIR}/build

cmake $SCRIPT_DIR && make || echo "rip"

