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

set datestr=%date%
set "date_today=%datestr:* =%"
set "commit_message=Automated update for %date_today%"

git add .
git commit -m "%commit_message%" >> %LOG_FILE%
git push  >> %LOG_FILE%