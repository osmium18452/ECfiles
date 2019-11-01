#!/usr/bin/env bash

dir=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

cd $dir/../..

userName=`cat ./set/userName`

sed -i "s/XXX/$userName/g" ./set/link2oj.desktop

parallel-ssh -t 1 -h ./iplist -v "mkdir ~$userName/.cache ~$userName/.local/share/gvfs-metadata -p"
parallel-scp -t 1 -h ./iplist -v ./set/link2oj.desktop /home/$userName/Desktop/link2oj.desktop
parallel-scp -t 1 -h ./iplist -v ./set/icon2oj.png /home/$userName/.cache/icon2oj.png
parallel-ssh -t 1 -h ./iplist -v "chmod +x ~$userName/Desktop/link2oj.desktop && rm -f ~$userName/.local/share/gvfs-metadata/home"
parallel-scp -t 1 -h ./iplist -v ./set/home /home/$userName/.local/share/gvfs-metadata/
parallel-ssh -t 1 -h ./iplist -v "chown $userName:$userName /home/$userName/ -R"

sed -i "s/$userName/XXX/g" ./set/link2oj.desktop
