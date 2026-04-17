#!/bin/bash
JUPYTER_TOKEN="${JUPYTER_TOKEN:-}"

NOTEBOOK_DIR="/home/user/app"

# Clear any cached workspace so default_url actually wins
rm -rf "$HOME/.jupyter/lab/workspaces" 2>/dev/null || true

# Generate a Welcome notebook from README.md so visitors land on rendered content.
# Notebook tabs render markdown far more reliably than opening a bare .md file.
python3 - <<'PY'
import json, pathlib
src = pathlib.Path('/home/user/app/README.md').read_text(encoding='utf-8')
# Strip the HF Space YAML frontmatter so only the real content is shown
if src.startswith('---'):
    end = src.find('\n---', 3)
    if end != -1:
        src = src[end + 4:].lstrip()
nb = {
    'cells': [{'cell_type': 'markdown', 'metadata': {}, 'source': src}],
    'metadata': {
        'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}
    },
    'nbformat': 4,
    'nbformat_minor': 5,
}
pathlib.Path('/home/user/app/Welcome.ipynb').write_text(
    json.dumps(nb, ensure_ascii=False), encoding='utf-8')
PY

jupyter labextension disable "@jupyterlab/apputils-extension:announcements"

jupyter-lab \
    --ip 0.0.0.0 \
    --port 7860 \
    --no-browser \
    --allow-root \
    --ServerApp.token="$JUPYTER_TOKEN" \
    --ServerApp.password="" \
    --IdentityProvider.token="$JUPYTER_TOKEN" \
    --ServerApp.tornado_settings="{'headers': {'Content-Security-Policy': 'frame-ancestors *'}}" \
    --ServerApp.cookie_options="{'SameSite': 'None', 'Secure': True}" \
    --ServerApp.disable_check_xsrf=True \
    --ServerApp.default_url=/lab/tree/Welcome.ipynb \
    --LabApp.default_url=/lab/tree/Welcome.ipynb \
    --LabApp.news_url=None \
    --LabApp.check_for_updates_class="jupyterlab.NeverCheckForUpdate" \
    --notebook-dir=$NOTEBOOK_DIR
