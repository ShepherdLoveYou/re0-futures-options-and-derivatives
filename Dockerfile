FROM nvidia/cuda:12.5.1-cudnn-devel-ubuntu20.04

ENV DEBIAN_FRONTEND=noninteractive \
    TZ=Europe/Paris \
    CONDA_AUTO_UPDATE_CONDA=false \
    HOME=/home/user \
    PATH=/home/user/miniconda/bin:$PATH \
    PYTHONUNBUFFERED=1 \
    PYTHONNOUSERSITE=1 \
    JUPYTER_DATA_DIR=/home/user/.jupyter/data \
    JUPYTER_RUNTIME_DIR=/home/user/.jupyter/runtime \
    IPYTHONDIR=/home/user/.jupyter/ipython \
    MPLCONFIGDIR=/home/user/.jupyter/matplotlib \
    GRADIO_ALLOW_FLAGGING=never \
    GRADIO_NUM_PORTS=1 \
    GRADIO_SERVER_NAME=0.0.0.0 \
    GRADIO_THEME=huggingface \
    SYSTEM=spaces \
    SHELL=/bin/bash

# Base utilities
RUN rm -f /etc/apt/sources.list.d/*.list && \
    apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    sudo \
    git \
    wget \
    procps \
    git-lfs \
    zip \
    unzip \
    htop \
    vim \
    nano \
    bzip2 \
    libx11-6 \
    build-essential \
    libsndfile-dev \
    software-properties-common \
 && rm -rf /var/lib/apt/lists/*

# nvtop
RUN add-apt-repository ppa:flexiondotorg/nvtop && \
    apt-get update && \
    apt-get install -y --no-install-recommends nvtop && \
    rm -rf /var/lib/apt/lists/*

# Node.js 21
RUN curl -fsSL https://deb.nodesource.com/setup_21.x | bash - && \
    apt-get update && \
    apt-get install -y nodejs && \
    npm install -g configurable-http-proxy && \
    rm -rf /var/lib/apt/lists/*

# Working directory
WORKDIR /app

# User setup — no sudo grant, so visitors can't escalate to modify app files
RUN adduser --disabled-password --gecos '' --shell /bin/bash user && \
    mkdir -p /home/user/.cache /home/user/.config /home/user/app && \
    chown -R user:user /home/user /app

# Miniconda Python 3.10
USER user
RUN curl -fsSL -o /home/user/miniconda.sh https://repo.anaconda.com/miniconda/Miniconda3-py310_22.11.1-1-Linux-x86_64.sh && \
    bash /home/user/miniconda.sh -b -p /home/user/miniconda && \
    rm -f /home/user/miniconda.sh && \
    conda clean -ya

WORKDIR /home/user/app

# Back to root for system packages / startup
USER root

RUN --mount=target=/root/packages.txt,source=packages.txt \
    apt-get update && \
    xargs -r -a /root/packages.txt apt-get install -y --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

RUN --mount=target=/root/on_startup.sh,source=on_startup.sh,readwrite \
    bash /root/on_startup.sh

RUN mkdir -p /data && chown user:user /data

# Python packages
USER user
RUN --mount=target=requirements.txt,source=requirements.txt \
    pip install --no-cache-dir --upgrade -r requirements.txt

# App files
COPY --chown=user:user . /home/user/app

# Bake a Welcome.ipynb from README.md before the directory is locked down
RUN python3 /home/user/app/_generate_welcome.py

RUN chmod +x /home/user/app/start_server.sh

# Comprehensive lockdown. The runtime `user` account can traverse /home/user
# and read everything, but can only write inside /home/user/.jupyter (which
# we pre-create). Every other path visitors might use to poison the shared
# container is root-owned and non-writable.
USER root
RUN \
    # App tree (notebooks, README, scripts).
    chown -R root:root /home/user/app && \
    chmod -R a-w,a+rX /home/user/app && \
    # Python runtime: prevents pip-overwrite and python-shim attacks.
    chown -R root:root /home/user/miniconda && \
    chmod -R a-w,a+rX /home/user/miniconda && \
    # Shared caches / config.
    chown -R root:root /home/user/.cache /home/user/.config && \
    chmod -R a-w,a+rX /home/user/.cache /home/user/.config && \
    # HF persistent-storage mount — unused by this project; lock so visitors
    # can't persist attack payloads across container restarts.
    chown root:root /data && \
    chmod 555 /data && \
    # Pre-create .local as root-owned + mode 555 so `pip install --user`
    # fails with permission error (belt-and-braces with PYTHONNOUSERSITE=1).
    mkdir -p /home/user/.local && \
    chown root:root /home/user/.local && \
    chmod 555 /home/user/.local && \
    # Writable exception: Jupyter's state dir. Pre-create the redirected
    # subdirs as user-owned so Jupyter doesn't try to mkdir a path whose
    # parent it doesn't own.
    mkdir -p /home/user/.jupyter/data \
             /home/user/.jupyter/runtime \
             /home/user/.jupyter/ipython \
             /home/user/.jupyter/matplotlib \
             /home/user/.jupyter/lab/workspaces \
             /home/user/.jupyter/lab/user-settings && \
    chown -R user:user /home/user/.jupyter && \
    chmod 755 /home/user/.jupyter && \
    # Top-level /home/user: traversable + readable, but NOT writable by user.
    # Done last so we don't lose the ability to mkdir/chown inside it above.
    chown root:root /home/user && \
    chmod 755 /home/user
USER user

# Jupyter template path for Python 3.10
COPY --chown=user:user login.html /home/user/miniconda/lib/python3.10/site-packages/jupyter_server/templates/login.html

CMD ["./start_server.sh"]
