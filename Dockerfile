FROM ubuntu:noble 

COPY requirements.txt requirements.txt

RUN apt update && \
    apt upgrade && \ 
    apt -y --no-install-recommends install \
        psmisc fuse libfuse-dev libfuse3-dev \ 
        python3 python3-pip

RUN pip3 install -r requirements.txt --break-system-packages
