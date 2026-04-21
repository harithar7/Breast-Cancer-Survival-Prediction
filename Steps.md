# Steps to Run This Project in VS Code (Windows)

This guide gives exact, granular steps to run the project from start to finish in Visual Studio Code.

## 1. Prerequisites

Install these first:
- Python 3.9 or above
- Visual Studio Code
- VS Code Python extension (Microsoft)

## 2. Open the Project in VS Code

1. Open VS Code.
2. Click File > Open Folder.
3. Select the folder:
   - C:/Users/erram/Desktop/pytho.sem4/Python_proj
4. Confirm you can see these files in Explorer:
   - Breast_Cancer.csv
   - EDA.py
   - Correlation.py
   - Visaulization.py
   - testing.py
   - SLR.py
   - sceniro.py

## 3. Open Integrated Terminal

1. In VS Code, click Terminal > New Terminal.
2. Ensure terminal path is the project root:
   - C:/Users/erram/Desktop/pytho.sem4/Python_proj

If not, run:

```powershell
cd C:/Users/erram/Desktop/pytho.sem4/Python_proj
```

## 4. Create Virtual Environment (First Time Only)

Run:

```powershell
# python -m venv .venv 
```

This creates a local Python environment in the .venv folder.

## 5. Activate Virtual Environment

In PowerShell terminal, run:

```powershell
# .\.venv\Scripts\Activate.ps1 -> This step is very important - explanation: To isolate the Dependency in a virtual environment.
```

After activation, your prompt should start with (.venv).

## 6. Select Python Interpreter in VS Code

1. Press Ctrl+Shift+P.
2. Type: Python: Select Interpreter
3. Choose interpreter from:
   - .venv/Scripts/python.exe

This ensures Run buttons and terminal use the same environment.

## 7. Install Project Dependencies

Run:

```powershell
pip install numpy pandas matplotlib seaborn scipy scikit-learn
```

Optional check:

```powershell
pip list
```

## 8. Run the Scripts (Recommended Order)

Run each command in the same terminal:

```powershell
python EDA.py
python Correlation.py
python Visaulization.py
python testing.py
python SLR.py
python sceniro.py
```

## 9. What to Expect for Each Script

1. EDA.py
- Prints shape, dtypes, summaries, missing values, duplicates, skewness, and outlier counts.

2. Correlation.py
- Prints correlation matrix and opens a heatmap plot.

3. Visaulization.py
- Opens 4 plots: age histogram, tumor boxplot, stage countplot, estrogen stacked bar.

4. testing.py
- Prints t-test statistic, p-value, and hypothesis decision.

5. SLR.py
- Prints regression equation, R2, RMSE, and opens regression plot.

6. sceniro.py
- Prints high-risk and low-risk metrics and stage-wise mortality percentages.

## 10. Run from VS Code Run Button (Alternative)

If you prefer the Run icon:

1. Open any script (for example EDA.py).
2. Click Run Python File (top-right play icon).
3. Repeat for each script in order.

Important:
- Keep the selected interpreter as .venv.
- Keep terminal working directory as project root.

## 11. Common Errors and Exact Fixes

1. Error: ModuleNotFoundError
- Cause: Packages not installed in active interpreter.
- Fix:

```powershell
pip install numpy pandas matplotlib seaborn scipy scikit-learn
```

2. Error: FileNotFoundError: Breast_Cancer.csv
- Cause: Running from wrong directory.
- Fix:

```powershell
cd C:/Users/erram/Desktop/pytho.sem4/Python_proj
```

Then rerun the script.

3. Plot window not opening
- Cause: Non-GUI/remote environment.
- Fix: Run locally in desktop VS Code with normal Python installation.

## 12. Verify Setup is Correct

Run this quick check:

```powershell
python -c "import pandas, numpy, matplotlib, seaborn, scipy, sklearn; print('Setup OK')"
```

Expected output:
- Setup OK

## 13. Optional: Save Dependency Snapshot

To export current packages:

```powershell
pip freeze > requirements.txt
```

To install later from file:

```powershell
pip install -r requirements.txt
```

## 14. Files to Read for Project Context

- README.md
- Project_Report.md

## 15. Optional One-Click Run

You can also run the project by double-clicking:

run_project.bat

This batch file will:
- create the virtual environment if needed
- activate it
- install dependencies
- run every analysis script in order

## 16. Parallel Plot Run

If you want the three plot graphs to open together, double-click:

Tryme.bat

This batch file will:
- create the virtual environment if needed
- activate it
- install dependencies
- launch Correlation.py, Visaulization.py, and SLR.py in parallel

These explain project goals, analysis results, and interpretation.
