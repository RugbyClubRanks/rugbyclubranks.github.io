@echo off
set LOG_FILE=update.log
echo. > %LOG_FILE%

pytest test_contents.py -o log_cli=true -o log_cli_level=DEBUG >> %LOG_FILE% 2>&1

if %errorlevel% neq 0 (
    echo Tests failed. Stopping the script. >> %LOG_FILE%
    exit /b %errorlevel%
) else (
    echo All tests passed. >> %LOG_FILE%
)

for /f "delims=" %%A in ('wmic os get localdatetime ^| find "."') do set datetime=%%A
set "date_today=%datetime:~0,4%-%datetime:~4,2%-%datetime:~6,2%"
set "commit_message=Automated update for %date_today%"

echo "%commit_message%" >> %LOG_FILE%