#define FUSE_USE_VERSION 31

#include <fuse/fuse.h>

#include <iostream>
#include <cstring>
#include <unistd.h>

static void show_help(const char *progname) {
    std::cerr << "usage: " << progname << " <mountpoint> [options]\n";
};


static int my_fuse_getattr (const char* path, struct stat* stbuf) {
    int res = 0;
    std::cout << "PATH IS " << path << "\n";
    std::memset(stbuf, '\0', sizeof(struct stat));

    stbuf->st_mode =  S_IFDIR | 0755;
    stbuf->st_nlink = 2;
    stbuf->st_size = 4096;  
    stbuf->st_uid = getuid();
    stbuf->st_gid = getgid();
    stbuf->st_atime = time(NULL);
    stbuf->st_mtime = time(NULL);
    return res;
};

static void *my_fuse_init(struct fuse_conn_info *conn) {
    (void) conn;
    std::cout << "INIT\n";
    return NULL;
};


static const struct fuse_operations my_fuse_oper = {
    .getattr = my_fuse_getattr,
    .init = my_fuse_init,
};  

int main(int argc, char *argv[]) {
    if (argc < 2) {
        show_help(argv[0]);
        return 1;
    }

    struct fuse_args args = FUSE_ARGS_INIT(argc, argv);
    int ret = fuse_main(args.argc, args.argv, &my_fuse_oper, NULL);
    fuse_opt_free_args(&args);

    return ret;
}