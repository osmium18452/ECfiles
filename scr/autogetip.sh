#!/usr/bin/env bash

while (true); do
	netplan apply
	sleep 60
done
