@echo off
REM Deploy Modern Dashboard V2 to GitHub + Render
cd /d "%~dp0"

echo ============================================
echo    DEPLOY MODERN DASHBOARD V2
echo ============================================
echo.

echo [1/4] Adding files to git...
git add .

echo.
echo [2/4] Committing changes...
git commit -m "V2 Modern Dashboard - 30+ metrics with vibrant design

- Complete redesign with cyan/orange/violet color scheme
- 30+ institutional metrics (Sharpe, Sortino, Calmar, VaR, CVaR, Kelly, etc.)
- 3 hero cards with glow effects
- Multiple chart types (Equity, Bar, Donut)
- Educational tooltips with metric explanations
- Professional grid layout
- FTMO compliance checks
- Advanced metrics (Recovery Factor, Ulcer Index, Pain Index)

Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>
"

echo.
echo [3/4] Pushing to GitHub...
git push

echo.
if errorlevel 0 (
    echo ============================================
    echo    SUCCESS!
    echo ============================================
    echo.
    echo V2 Dashboard pushed to GitHub!
    echo.
    echo Render will auto-deploy in 30 seconds...
    echo Check: https://dashboard.render.com
    echo.
    echo Once deployed, test with TEST_AGENTS_DATA.zip!
    echo.
) else (
    echo ============================================
    echo    FAILED!
    echo ============================================
    echo.
    echo Check your git config and try again.
    echo.
)

pause
