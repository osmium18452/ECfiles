#!/usr/bin/env bash

while (true); do
    pssh -h /home/acm/workspace/acm/iplist -t 2 'killall gdm-session-work'
    sleep 60
done
