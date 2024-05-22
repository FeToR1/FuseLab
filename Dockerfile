FROM ubuntu:noble 

RUN apt update && \
    apt upgrade && \ 
    apt -y --no-install-recommends install \
        build-essential clang cmake gdb \ 
        psmisc fuse libfuse-dev libfuse3-dev \ 
        python3 python3-pip


