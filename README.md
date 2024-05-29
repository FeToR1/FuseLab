# Description

* The path to the directory with pictures in PNG format transfers to your program to receive initial files from there.

* Listing a directory, your program should list the original files and their converted copies if applicable.

* When trying to open a JPG file, the original PNG should be converted and returned as a JPG format and reverse.

* All other operations must transfer to the original directory. For example, `mkdir mounted_dir/new_dir` will create a directory in `original_dir`.

# Setup

## Docker

``` bash
docker-compose up -d 
docker exec -it fuse_ubuntu bash
```

## Linux

``` bash
mkdir -p /mounted_dir
pip3 install -r requirements.txt
python3 /source/main.py /original_dir /mounted_dir &
```

## Windows

1. Install normal OS
2. PROFIT

# Run

work in /mounted_dir
