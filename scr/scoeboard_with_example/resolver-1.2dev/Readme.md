# Readme - for resolver

## Environment

    Python
        version >= 3.6.x
        Request - HTTPBasicAuth
        xml
        json

    Java Virtual Machine
        version >= 1.7 

    Windows 7/8/10 or Ubuntu 16.x+

    Recommand RAM >= 8G

## File structure

    ./resolver-1.x
    ├── Readme.md                - This README file
    ├── awards.bat               - Manually run resolver(for Windows)
    ├── awards.sh                - Manually run resolver(for Linux)
    ├── cdp
    │   ├── contest.xml          - Processed contest info
    │   └── images              
    │       ├── logo             - Put school logos in this directory
    │       │   └── *.png
    |       |
    |       |       /*********************************************************/
    |       |           Format:
    |       |               Size:       600 * 600 px suggested
    |       |               Filename:   <school_id>.png 
    |       |                           - Afiiliation ID in domjudge database
    |       |               *Special(for better performance, not necessary):
    |       |                           Inside logo:    white background
    |       |                           Outside logo:   transparent
    |       |       /*********************************************************/
    |       |
    │       └── team            - Put team photos in this directory
    │           └── *.jpg
    |       |
    |       |       /*********************************************************/
    |       |           Format:
    |       |               Size:       1920 * 1080 px suggested
    |       |               Filename:   <team_id>.png 
    |       |                           - Team ID in domjudge database
    |       |               *Special(for better performance, not necessary):
    |       |                           Please refer photo format
    |       |       /*********************************************************/
    |       └─
    ├── lib\                     - resolver lib
    ├── logs\                    - resolver log
    ├── feed.py                  - Fetch contest info
    ├── main_file.py             - Process team name
    ├── process_unjudged_run.py  - Process invalid data
    └── runresolver.bat          - Start resolver

## Steps

- Set arguments in feed.py
  - <ip_addr> - host ip of domjudge server
  - <event_reader_username> - Username for account with (Internal/System)full_event_reader privilege
  - <event_reader_password> - Password for account with (Internal/System)full_event_reader privilege

- Run feed.py
  - Generate ext.xml in current directory

- Set arguments in runresolver.bat
  - <gold/silver/bronze_rank> - Rank for gold/silver/bronze prize
    - !!! PRIZE RANK instead of prize number !!!
    - !!! Ignore STARRED team !!!
  - <first_prize_citation> - Title for first prize

- Run runresolver.bat
  - Follow the instruction
  - If everything goes well, "Ready to start..." will be shown on screen

- Double check EVERYTHING then press any key to start

- runresolver.bat will automatically remove temp file when finished
