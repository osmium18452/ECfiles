#!/usr/bin/env bash

dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

cd $dir/..

userName=`cat ./set/userName`

pssh -h ./iplist "mkdir /home/$userName/.config"
pscp -r -h ./iplist ./set/codeblocks /home/$userName/.config/
pssh -h ./iplist "chown -R $userName:$userName /home/$userName"
