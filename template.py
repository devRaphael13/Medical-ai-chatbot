import os
from pathlib import Path

files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "requirements.txt",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]

for filepath in files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir:
        os.makedirs(filedir, exist_ok=True)

    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            pass