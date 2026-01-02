@echo off
REM Ujjivan Small Finance Bank Setup Script for Windows
REM This script will set up the Ujjivan custom template system

echo ==============================================
echo   Ujjivan Small Finance Bank Setup
echo ==============================================
echo.

REM Check if we're in the right directory
if not exist "app.py" (
    echo [ERROR] app.py not found. Please run this script from the land-valuation directory.
    pause
    exit /b 1
)

echo [INFO] Pre-flight Checks
echo ----------------------------------------------

REM Check if Python is available
python --version >nul 2>&1
if %errorlevel% equ 0 (
    echo [OK] Python is installed
    set PYTHON_CMD=python
) else (
    python3 --version >nul 2>&1
    if %errorlevel% equ 0 (
        echo [OK] Python3 is installed
        set PYTHON_CMD=python3
    ) else (
        echo [ERROR] Python is not installed
        pause
        exit /b 1
    )
)

REM Check if virtual environment exists
if exist "venv\Scripts\activate.bat" (
    echo [INFO] Activating virtual environment...
    call venv\Scripts\activate.bat
    echo [OK] Virtual environment activated
) else (
    echo [WARNING] Virtual environment not found at venv\Scripts\activate.bat
    echo [INFO] Continuing without virtual environment...
)

REM Check if database exists
if exist "land_valuation.db" (
    echo [OK] Database file found
) else (
    echo [WARNING] Database file not found. It will be created.
)

echo.
echo [INFO] Backing Up Database
echo ----------------------------------------------

REM Backup database if it exists
if exist "land_valuation.db" (
    set BACKUP_FILE=land_valuation.db.backup.%date:~-4,4%%date:~-10,2%%date:~-7,2%_%time:~0,2%%time:~3,2%%time:~6,2%
    set BACKUP_FILE=%BACKUP_FILE: =0%
    copy land_valuation.db "%BACKUP_FILE%" >nul
    echo [OK] Database backed up to: %BACKUP_FILE%
) else (
    echo [WARNING] No database to backup
)

echo.
echo [INFO] Running Migration
echo ----------------------------------------------

REM Run the migration script
%PYTHON_CMD% migrate_ujjivan_fields.py

if %errorlevel% equ 0 (
    echo [OK] Migration completed successfully
) else (
    echo [ERROR] Migration failed
    echo Please check the error messages above and try again.
    pause
    exit /b 1
)

echo.
echo [INFO] Verifying Installation
echo ----------------------------------------------

REM Check if template files exist
if exist "templates\ujjivan_valuation_form.html" (
    echo [OK] Ujjivan form template found
) else (
    echo [ERROR] Ujjivan form template not found
)

if exist "templates\ujjivan_report.html" (
    echo [OK] Ujjivan report template found
) else (
    echo [ERROR] Ujjivan report template not found
)

echo.
echo ==============================================
echo [SUCCESS] Setup Complete!
echo ==============================================
echo.
echo Next Steps:
echo 1. Start your Flask application:
echo    %PYTHON_CMD% app.py
echo.
echo 2. Access the Ujjivan form at:
echo    http://localhost:5000/valuation/new?bank=ujjivan
echo.
echo 3. Or select 'Ujjivan Small Finance Bank' from the
echo    bank dropdown in the regular form
echo.
echo For detailed documentation, see:
echo    UJJIVAN_SETUP_GUIDE.md
echo.
echo ==============================================
echo.
pause

