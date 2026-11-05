@echo off
title THE FLOOR IS FOLLOWING YOU
cd /d "%~dp0"
echo Starting THE FLOOR IS FOLLOWING YOU...
python main.py
if %ERRORLEVEL% neq 0 (
    echo.
    echo Game exited with code %ERRORLEVEL%.
    pause
)
