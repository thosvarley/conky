#!/bin/bash 

if ! test -f conky.conf; then 
    ./buildconky.sh
fi

conky -c ~/.conky/conky.conf
