# HF Spaces Docker image for the Re:0 derivatives tutorial.
# Slim python base — the notebooks are CPU-only, no GPU / conda needed.
FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive \
    TZ=UTC \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONNOUSERSITE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    HOME=/home/user \
    JUPYTER_DATA_DIR=/home/user/.jupyter/data \
    JUPYTER_RUNTIME_DIR=/home/user/.jupyter/runtime \
    IPYTHONDIR=/home/user/.jupyter/ipython \
    MPLCONFIGDIR=/home/user/.jupyter/matplotlib \
    SHELL=/bin/bash

# Minimal system packages. `tini` for clean PID-1 signal handling,
# `git` so cells that reference sub-repos still work if the user clones one.
RUN apt-get update && apt-get install -y --no-install-recommends \
        ca-certificates \
        git \
        tini \
        tree \
    && rm -rf /var/lib/apt/lists/*

# Non-root runtime user. UID 1000 matches the HF Spaces convention.
# No sudo grant — visitors execute code as `user` with no path to escalate.
RUN useradd --create-home --shell /bin/bash --uid 1000 user

# Python deps installed system-wide so site-packages is root-owned by default
# (no extra chown step needed in the lockdown below).
COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip \
 && pip install -r /tmp/requirements.txt \
 && rm /tmp/requirements.txt

WORKDIR /home/user/app

# App files — copied as `user` so the Welcome-generator step can write
# Welcome.ipynb alongside the chapter notebooks before the lockdown.
COPY --chown=user:user . /home/user/app

# Bake Welcome.ipynb from the chapter list into the image.
RUN python3 /home/user/app/_generate_welcome.py

RUN chmod +x /home/user/app/start_server.sh

# Comprehensive lockdown. The runtime `user` can read + execute everything
# but can only write inside /home/user/.jupyter (pre-created below). Every
# other path a visitor might use to poison the shared container is
# root-owned and non-writable.
RUN set -eu && \
    # App tree (notebooks, README, scripts).
    chown -R root:root /home/user/app && \
    chmod -R a-w,a+rX /home/user/app && \
    # Shared caches / config.
    mkdir -p /home/user/.cache /home/user/.config && \
    chown -R root:root /home/user/.cache /home/user/.config && \
    chmod -R a-w,a+rX /home/user/.cache /home/user/.config && \
    # Root-owned .local so `pip install --user` fails with PermissionError
    # (belt-and-braces with PYTHONNOUSERSITE=1).
    mkdir -p /home/user/.local && \
    chown root:root /home/user/.local && \
    chmod 555 /home/user/.local && \
    # Writable exception: Jupyter's state dir, redirected via the ENV
    # vars above. Pre-create as user-owned.
    mkdir -p /home/user/.jupyter/data \
             /home/user/.jupyter/runtime \
             /home/user/.jupyter/ipython \
             /home/user/.jupyter/matplotlib \
             /home/user/.jupyter/lab/workspaces \
             /home/user/.jupyter/lab/user-settings && \
    chown -R user:user /home/user/.jupyter && \
    chmod 755 /home/user/.jupyter && \
    # Top-level /home/user: traversable but not user-writable. Done last
    # so we don't lose the ability to mkdir/chown its children above.
    chown root:root /home/user && \
    chmod 755 /home/user

USER user

EXPOSE 7860

ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["./start_server.sh"]
