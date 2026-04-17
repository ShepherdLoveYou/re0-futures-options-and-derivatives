"""Build-time helper: bake a Welcome.ipynb from README.md into the image.

Invoked by the Dockerfile so the Space lands on a rendered notebook
regardless of JupyterLab workspace state. Strips the HF Space YAML
frontmatter so only the real README body is shown.
"""

import json
import pathlib

APP_DIR = pathlib.Path("/home/user/app")

src = (APP_DIR / "README.md").read_text(encoding="utf-8")
if src.startswith("---"):
    end = src.find("\n---", 3)
    if end != -1:
        src = src[end + 4 :].lstrip()

nb = {
    "cells": [{"cell_type": "markdown", "metadata": {}, "source": src}],
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3",
        }
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}

(APP_DIR / "Welcome.ipynb").write_text(
    json.dumps(nb, ensure_ascii=False), encoding="utf-8"
)
