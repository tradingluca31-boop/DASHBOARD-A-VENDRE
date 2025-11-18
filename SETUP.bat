@echo off
REM Change to script directory
cd /d "%~dp0"

echo ============================================
echo    TRADING DASHBOARD PRO - Setup
echo ============================================
echo.

REM Check Python
echo [1/4] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found!
    echo Please install Python 3.8+ from python.org
    pause
    exit /b 1
)
python --version
echo.

REM Create virtual environment
echo [2/4] Creating virtual environment...
if exist "venv_dashboard" (
    echo Virtual environment already exists, skipping...
) else (
    python -m venv venv_dashboard
    echo Virtual environment created!
)
echo.

REM Activate and install dependencies
echo [3/4] Installing dependencies...
call venv_dashboard\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt
echo.

REM Create .env file if not exists
echo [4/4] Configuring environment...
if not exist ".env" (
    echo Creating .env file from template...
    copy .env.example .env
    echo.
    echo [IMPORTANT] Please edit .env file with your settings!
    echo.
) else (
    echo .env file already exists, skipping...
)

echo.
echo ============================================
echo    Setup Complete!
echo ============================================
echo.
echo Next steps:
echo   1. Edit .env file with your configuration
echo   2. Run START_DASHBOARD.bat to launch
echo.
pause
