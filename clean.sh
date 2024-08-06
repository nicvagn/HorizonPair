#!/usr/bin/env bash
    
cd $( dirname $( readlink -m $( type -p ${0} )))

rm -r ./build/*

