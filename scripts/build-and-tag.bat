@echo off
set /p tag="Enter tag (e.g., dev, prod): "

REM Format date as YYYYMMDD
for /f %%a in ('powershell -command "Get-Date -Format yyyyMMdd"') do set datestamp=%%a

REM Set image name and full tag
set imagename=quant-capstone
set fulltag=%imagename%:%tag%-%datestamp%

echo Building image: %fulltag%

REM Build and tag the image once
docker build -t %fulltag% .

REM Ask if user wants to tag it as something simpler (like "dev")
set /p simpletag="Add additional tag (optional, e.g., dev): "

IF NOT "%simpletag%"=="" (
    docker tag %fulltag% %imagename%:%simpletag%
    echo Tagged as: %imagename%:%simpletag%
)

echo Done.
pause


@REM run with: .\scripts\build-and-tag.bat
