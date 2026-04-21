@echo off
setlocal

cd /d "%~dp0"
set "PYTHON_EXE=%~dp0.venv\Scripts\python.exe"

if not exist "%PYTHON_EXE%" (
    echo Virtual environment not found.
    echo Creating .venv...
    python -m venv .venv
    if errorlevel 1 (
        echo Failed to create virtual environment.
        pause
        exit /b 1
    )
)

if not exist "%PYTHON_EXE%" (
    echo Python executable still not found inside .venv.
    pause
    exit /b 1
)

echo Installing required packages...
"%PYTHON_EXE%" -m pip install numpy pandas matplotlib seaborn scipy scikit-learn
if errorlevel 1 (
    echo Package installation failed.
    pause
    exit /b 1
)

echo.
echo Launching three plot scripts in parallel...
echo Close the plot windows when you finish reviewing them.
echo.

start "Correlation Plot" "%PYTHON_EXE%" Correlation.py
start "Visualization Plot" "%PYTHON_EXE%" Visaulization.py
start "Regression Plot" "%PYTHON_EXE%" SLR.py

echo All three plot scripts have been launched in parallel.
pause
