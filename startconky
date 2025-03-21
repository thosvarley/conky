#!/bin/bash 

if ! test -f conky.conf; then
    touch conky.conf 
    python buildconky.py
fi

conky -c ~/.conky/conky.conf
