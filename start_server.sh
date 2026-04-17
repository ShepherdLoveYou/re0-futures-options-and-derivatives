#!/bin/bash
JUPYTER_TOKEN="${JUPYTER_TOKEN:-}"

NOTEBOOK_DIR="/home/user/app"

# Make .md files open as rendered Markdown Preview instead of raw editor
SETTINGS_DIR="$HOME/.jupyter/lab/user-settings/@jupyterlab/docmanager-extension"
mkdir -p "$SETTINGS_DIR"
cat > "$SETTINGS_DIR/plugin.jupyterlab-settings" <<'JSON'
{
  "defaultViewers": {
    "markdown": "Markdown Preview"
  }
}
JSON

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
    --ServerApp.default_url='/lab/tree/README.md?reset' \
    --LabApp.default_url='/lab/tree/README.md?reset' \
    --LabApp.news_url=None \
    --LabApp.check_for_updates_class="jupyterlab.NeverCheckForUpdate" \
    --notebook-dir=$NOTEBOOK_DIR
