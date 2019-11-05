#!/usr/bin/bash

echo "Notice: You must finalize contest before export ext.xml"
echo "Notice: Put processed Images to ./cdp/image/ directory"
echo "Press any key to continue..."
read -n 1

filename="xml"
echo "Processing team name(Generate ext2.xml)"
python3 main_file.py

echo "Processing unjudged runs(Generate out.xml)"
python3 process_unjudged_run.py

echo "Generating scoreboard info - Please make sure MEDAL NUMBER is CORRECT!"
echo "Press anke key to continune..."
read -n 1
./award.sh ${filename}.xml --medals <gold_rank> <silver_rank> <bronze_rank> --firstPlaceCitation "<first-place_citation>" --fts true true
echo "Ready to start, press any key to run resolver..."
read -n 1

mv ${filename}-awards.xml ./cdp/contest.xml
./resolver.sh cdp --fast 0.1 --singleStep 18

echo "Removing temp files..."
rm ext2.xml
rm out.xml
echo "Process done, press any key to exit"
read -n 1
