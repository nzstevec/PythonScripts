# Make a virtual environment

`py -m venv .venv`

# Activate the environment

`source .venv/Scripts/activate`

# Install pyinstaller

`pip install pyinstaller`

# Make exe

`pyistaller --onefile creds_download.py`

`pyistaller --onefile creds_switch.py`

# Copy exe's from dist folder to PATH