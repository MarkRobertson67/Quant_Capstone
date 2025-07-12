@echo off
docker run --name quant-dev -v "%cd%\output:/app/output" quant-capstone:dev
@REM  --rm  (add after run if I  want to remove container after running)

@REM run with: .\scripts\run.bat
