@echo off
REM Change to script directory
cd /d "%~dp0"

echo ============================================
echo    CREATE TEST ZIP FOR DASHBOARD
echo ============================================
echo.

REM Check if PowerShell is available
where powershell >nul 2>&1
if errorlevel 1 (
    echo [ERROR] PowerShell not found!
    pause
    exit /b 1
)

echo [1/2] Collecting test data files...
if not exist "test_data_agent7.json" (
    echo [ERROR] test_data_agent7.json not found!
    pause
    exit /b 1
)

if not exist "test_data_agent8.json" (
    echo [ERROR] test_data_agent8.json not found!
    pause
    exit /b 1
)

echo [2/2] Creating ZIP file...
powershell -Command "Compress-Archive -Path 'test_data_agent7.json','test_data_agent8.json' -DestinationPath 'TEST_AGENTS_DATA.zip' -Force"

if exist "TEST_AGENTS_DATA.zip" (
    echo.
    echo ============================================
    echo    SUCCESS!
    echo ============================================
    echo.
    echo ZIP file created: TEST_AGENTS_DATA.zip
    echo.
    echo You can now upload this ZIP to your dashboard:
    echo https://dashboard-a-vendre-XXXX.onrender.com
    echo.
    echo The ZIP contains:
    echo   - Agent 7 PPO (ROI: 22.8%%, Sharpe: 1.38)
    echo   - Agent 8 SAC (ROI: 16.8%%, Sharpe: 1.18)
    echo.
) else (
    echo.
    echo ============================================
    echo    FAILED!
    echo ============================================
    echo.
    echo Could not create ZIP file.
    echo.
)

pause
