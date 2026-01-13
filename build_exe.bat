@echo off
echo ========================================
echo Building Quadratic Calculator EXE
echo ========================================
echo.

pyinstaller --onefile --windowed --name "QuadraticCalculator" --icon=NONE --add-data "logic;logic" calc.py

echo.
echo ========================================
echo Build Complete!
echo EXE location: dist\QuadraticCalculator.exe
echo ========================================
pause
