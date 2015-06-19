#!/bin/bash

if [ "$USER" == "admin" ] || [ "$USER" == "root" ] || [ "$USER" == "" ];then
    echo ""
else
    python /opt/jumpserver/connect.py
    exit 3
    echo

fi
