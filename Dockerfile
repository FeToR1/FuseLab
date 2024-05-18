FROM ubuntu:noble 

RUN apt update && apt -y --no-install-recommends install \
    build-essential \
    clang \
    cmake \
    gdb \
    wget \
    curl \
    fuse \
    libfuse-dev \
    git \
    ca-certificates \
    gperf \
    zlib1g-dev \
    libssl-dev
