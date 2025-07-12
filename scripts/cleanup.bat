@echo off
echo 🔍 Checking Docker space usage before cleanup...
docker system df

echo.
echo 🛑 Removing all stopped containers...
docker container prune -f

echo 🧼 Removing all unused images (not just dangling)...
docker image prune -a -f

echo 🧹 Removing unused volumes...
docker volume prune -f

echo 💣 Final full cleanup: unused networks and build cache...
docker system prune -f

echo.
echo ✅ Cleanup complete!
echo 📊 Final Docker disk usage:
docker system df

pause

@REM run with: .\scripts\cleanup.bat
