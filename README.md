# melbourne-realestate

This is a tutorial project. The aim is to fit a ML model for a dataset from kaggle. Then, build a simple streamlit app on top of it.

# Pre-Requisits

- Download and install `git` from here: https://git-scm.com/downloads/win

# Set up the Project

```
git clone https://github.com/bmotevalli/melbourne-realestate.git
cd melbourne-realestate
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

# Data

Download the data for this project from below:

https://www.kaggle.com/datasets/dansbecker/melbourne-housing-snapshot

Locate the data in a subfolder `data`.

# Add .venv to notebook's kernel

```
pip install ipykernel
python -m ipykernel install --user --name=mel-realestate --display-name "mel-realestate"
```

# Add your project to PYTHONPATH

WinOS:

- Powershell

```powershell
$env:PYTHONPATH = "C:\path\to\your_project"
```

- CMD

```cmd
set PYTHONPATH=C:\path\to\your_project
```

macOS/Linux:

```bash
export PYTHONPATH="/path/to/your_project"
```

# Run the app

```
streamlit run app\views\main.py --server.runOnSave=true
```
