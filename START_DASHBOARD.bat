@echo off
REM Change to script directory
cd /d "%~dp0"

echo ============================================
echo    TRADING DASHBOARD PRO - Starting...
echo ============================================
echo.

REM Check if virtual environment exists
if not exist "venv_dashboard\Scripts\activate.bat" (
    echo [ERROR] Virtual environment not found!
    echo.
    echo Please run SETUP.bat first to create the environment.
    echo.
    pause
    exit /b 1
)

REM Activate virtual environment
echo [1/2] Activating virtual environment...
call venv_dashboard\Scripts\activate.bat

REM Start dashboard
echo [2/2] Starting dashboard...
echo.
echo ============================================
echo    Dashboard will open at:
echo    http://localhost:8050
echo ============================================
echo.
echo Press Ctrl+C to stop the dashboard
echo.

python app.py

pause
