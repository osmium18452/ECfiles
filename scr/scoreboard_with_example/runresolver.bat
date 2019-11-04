::python feed.py
@echo off
echo Notice: You must finalize contest before export ext.xml
echo Notice: Put processed Images to ./cdp/image directory
@pause
cls

set xml=out
echo Processing team name(ext2.xml)
python main_file.py

echo Processing unjuged runs(out.xml)
python process_unjudged_run.py

echo Generating scoreboard info - Please make sure MEDAL NUMBER is RIGHT!
@pause
call awards.bat %xml%.xml --medals <gold_rank> <silver_rank> <bronze_rank> --firstPlaceCitation "<first_palce_citation>" --fts true true
echo Ready to start...
@pause

move %xml%-awards.xml .\cdp\contest.xml
call resolver.bat cdp --fast 0.1 --singleStep 18

echo Removing temp files....
@pause
del ext2.xml
del out.xml