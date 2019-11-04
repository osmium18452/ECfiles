@echo off
rem
rem Purpose: to apply awards to an event feed 
rem

set LIBDIR=%~dp0\lib

set params=

:loop
if %1. == . goto :continue
set params=%params% %1
shift
goto :loop

:continue

java -jar "%LIBDIR%\swtLauncher.jar" resolver.jar org.acmicpc.resolver.awards.Awards %params%
