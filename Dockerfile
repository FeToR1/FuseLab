FROM ubuntu:noble 


RUN apt update && \
    apt upgrade && \ 
    apt -y --no-install-recommends install \
        build-essential clang cmake gdb \ 
        psmisc fuse libfuse-dev libfuse3-dev \ 
        python3 python3-pip


COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt --break-system-packages
