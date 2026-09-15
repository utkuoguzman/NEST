# Use NVIDIA CUDA development base image
FROM nvidia/cuda:12.2.0-devel-ubuntu22.04

# Avoid tzdata interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libzmq3-dev \
    libopenmpi-dev \
    openmpi-bin \
    git \
    cmake \
    python3 \
    python3-pip \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install standard scientific packages, standard NEST, BSB, and NEST-Desktop
RUN pip3 install --no-cache-dir \
    numpy \
    scipy \
    matplotlib \
    mpi4py \
    pyzmq \
    nest-simulator \
    "bsb[nest,parallel]" \
    nest-desktop \
    gunicorn \
    flask \
    flask-cors \
    RestrictedPython

# Install NEST-GPU from source
WORKDIR /opt
RUN git clone https://github.com/nest/nest-gpu.git && \
    cd nest-gpu && \
    mkdir build && cd build && \
    cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr/local .. && \
    make -j$(nproc) && \
    make install

# Set python environment path to include potential /usr/local installation locations
ENV PYTHONPATH=/usr/local/lib/python3.10/dist-packages:/usr/local/lib/python3.10/site-packages:${PYTHONPATH}
ENV NESTGPU_LIB=/usr/local/lib/nestgpu/libnestgpukernel.so

# Configure NEST Server for NEST Desktop
ENV NEST_SERVER_DISABLE_AUTH=true
ENV NEST_SERVER_ENABLE_EXEC_CALL=true
ENV NEST_SERVER_DISABLE_RESTRICTION=true

WORKDIR /workspace