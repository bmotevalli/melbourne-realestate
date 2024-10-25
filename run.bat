@echo off
REM Activate the virtual environment
call .venv\Scripts\activate

REM Set PYTHONPATH to the current directory
set PYTHONPATH=%cd%

REM Run the Streamlit app with auto-reload on save
streamlit run app\views\main.py --server.runOnSave=true
