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
