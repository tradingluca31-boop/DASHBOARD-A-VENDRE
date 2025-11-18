@echo off
REM Change to script directory
cd /d "%~dp0"

echo ============================================
echo    PUSH CODE TO GITHUB
echo ============================================
echo.

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Git not installed!
    echo Please install Git from: https://git-scm.com/download/win
    pause
    exit /b 1
)

echo [1/5] Removing old remote if exists...
git remote remove origin 2>nul

echo [2/5] Adding correct GitHub remote...
git remote add origin https://github.com/tradingluca31-boop/DASHBOARD-A-VENDRE.git

echo [3/5] Verifying remote URL...
git remote -v

echo.
echo [4/5] Adding all files...
git add .

echo.
echo [5/5] Committing changes...
git commit -m "Update dashboard code" 2>nul

echo.
echo ============================================
echo    READY TO PUSH!
echo ============================================
echo.
echo GitHub will ask for:
echo   Username: tradingluca31-boop
echo   Password: [YOUR GITHUB TOKEN]
echo.
echo If you don't have a token yet:
echo   1. Go to: https://github.com/settings/tokens
echo   2. Generate new token (classic)
echo   3. Check 'repo' scope
echo   4. Copy the token
echo.
pause

echo.
echo Pushing to GitHub...
git push -u origin main

echo.
if errorlevel 0 (
    echo ============================================
    echo    SUCCESS!
    echo ============================================
    echo.
    echo Your code is now on GitHub!
    echo Check: https://github.com/tradingluca31-boop/DASHBOARD-A-VENDRE
    echo.
    echo Render will auto-deploy in 30 seconds!
) else (
    echo ============================================
    echo    FAILED!
    echo ============================================
    echo.
    echo Possible reasons:
    echo   - Wrong GitHub token
    echo   - No internet connection
    echo   - Repository doesn't exist
    echo.
)

echo.
pause
